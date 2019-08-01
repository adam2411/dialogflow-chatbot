"""
* @author: Aditya Aman
* This file is recommended only for windows user
* to run the python application.
"""

from app import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
