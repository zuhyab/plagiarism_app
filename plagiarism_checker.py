from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, abort
from flask_login import login_required, current_user
import os
from difflib import SequenceMatcher

plagiarism_blueprint = Blueprint('plagiarism', __name__)
UPLOAD_FOLDER = 'static/uploads/'

@plagiarism_blueprint.route('/user_dashboard', methods=['GET', 'POST'])
@login_required
def user_dashboard():
    if current_user.is_admin:
        return redirect(url_for('plagiarism.admin_dashboard'))

    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            filename = os.path.basename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            flash("File uploaded successfully!")
        else:
            flash("No file selected!")

    files = os.listdir(UPLOAD_FOLDER) if os.path.exists(UPLOAD_FOLDER) else []
    return render_template('user_dashboard.html', username=current_user.username, files=files)

@plagiarism_blueprint.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('plagiarism.user_dashboard'))

    files = os.listdir(UPLOAD_FOLDER) if os.path.exists(UPLOAD_FOLDER) else []
    results = []

    if request.method == 'POST':
        if len(files) < 2:
            flash("Need at least 2 files to check for plagiarism!")
        else:
            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    try:
                        with open(os.path.join(UPLOAD_FOLDER, files[i]), 'r', encoding='utf-8', errors='ignore') as f1:
                            content1 = f1.read()
                        with open(os.path.join(UPLOAD_FOLDER, files[j]), 'r', encoding='utf-8', errors='ignore') as f2:
                            content2 = f2.read()

                        similarity_ratio = SequenceMatcher(None, content1, content2).ratio() * 100
                        results.append((files[i], files[j], round(similarity_ratio, 2)))
                    except Exception as e:
                        flash(f"Error comparing {files[i]} and {files[j]}: {str(e)}")

            if results:
                flash(f"Compared {len(results)} file pairs successfully!")

    return render_template('admin_dashboard.html', files=files, results=results)

@plagiarism_blueprint.route('/open/<filename>')
@login_required
def open_file(filename):
    safe_filename = os.path.basename(filename)
    file_path = os.path.join(UPLOAD_FOLDER, safe_filename)

    if not os.path.exists(file_path):
        abort(404)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        return render_template('view_file.html', filename=safe_filename, content=content)
    except Exception as e:
        flash(f"Unable to open file: {e}")
        return redirect(url_for('plagiarism.user_dashboard'))

@plagiarism_blueprint.route('/download/<filename>')
@login_required
def download_file(filename):
    safe_filename = os.path.basename(filename)
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, safe_filename)):
        abort(404)
    return send_from_directory(UPLOAD_FOLDER, safe_filename, as_attachment=True)
