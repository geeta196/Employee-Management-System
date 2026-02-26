from flask import request, jsonify
from models import db, Employee
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "uploads"

def register_routes(app):

    # GET all employees
    @app.route("/employees", methods=["GET"])
    def get_employees():
        employees = Employee.query.all()
        result = []

        for emp in employees:
            result.append({
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "position": emp.position,
                "salary": emp.salary,
                "image": emp.image
            })

        return jsonify(result)

    # ADD employee
    @app.route("/employees", methods=["POST"])
    def add_employee():
        try:
            file = request.files.get("image")
            filename = None

            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))

            emp = Employee(
                name=request.form["name"],
                email=request.form["email"],
                position=request.form.get("position"),
                salary=request.form.get("salary"),
                image=filename
            )

            db.session.add(emp)
            db.session.commit()

            return jsonify({"message": "Employee Added"}), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # DELETE employee
    @app.route("/employees/<int:id>", methods=["DELETE"])
    def delete_employee(id):
        emp = Employee.query.get(id)

        if not emp:
            return jsonify({"message": "Employee not found"}), 404

        db.session.delete(emp)
        db.session.commit()

        return jsonify({"message": "Employee Deleted"})