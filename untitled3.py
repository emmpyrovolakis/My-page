from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def starting():
    return """
    <html>
      <body style="font-family: Arial; font-size: 20px; text-align: center; background-color: #CCC0C6;">
        <h1>Welcome to my page</h1>
        <p>Emmanouil Pyrovolakis, Mathematician</p>
        <hr>
        <a href="/education">Σπουδές/Education -> </a> <br><br>
        <a href="/workexperience">Εργασία/Work Experience -></a>
      </body>
    </html>
    """

@app.route("/education")
def education():
    return """
    <html>
      <body style="font-family: Arial; font-size: 24px; text-align: center; background-color: #CCC0C6;">
        <h1>Education</h1>
        <a href="/"> <- Πίσω στην Αρχική</a><br><br>
        <p>-> University of Crete<br>
        Bachelor of Science, Mathematics<br>
        2022-2026<br>
        Grade: 7.57/10<br><br><br>
        ->1st High School of Souda<br>
        Greek<br>
        2019-2022<br>
        Grade: 19.1/20</p>
      </body>
    </html>
    """

@app.route("/workexperience")
def workexperience():
    return """
    <html>
      <body style="font-family: Arial; font-size: 18px; text-align: center; background-color: #CCC0C6;">
        <h1>Work Experience</h1>
        <a href="/"> <- Πίσω στην Αρχική</a><br><br>
        <p><b>Mathematics Tutor (2024-2026):</b><br> Experienced in teaching both high school and university students...</p>
        <p><b>Head Waiter (2023-2025):</b><br> Led service operations during high-demand seasons...</p>
        <p><b>Barista/Waiter (2021-2023):</b><br> Worked in high-demand peak tourist seasons...</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
