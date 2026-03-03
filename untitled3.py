from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def starting():
    return"""
    <html>
      <body style = "font-family: Arial;font-size: 20px; text-align: center; background-color: #CCC0C6;">
      <h1>Welcome to my page</h1>
        <p>Emmanouil Pyrovolakis, Mathematics</p>
        <hr>
        <a href="/education">Σπουδές/Education -> </a> <br><br>
        <a href="/workexperience">Εργασία/Work Experience -></a><br><br>
        <a href="/profesionallinks">Συνδέσμοι/Professional Links -></a><br><br>
        <a href="/interests">Ενδιαφέροντα/Academic Interests -></a><br><br>
        <a href="/communication">Στοιχεία Επικοινωνίας/Contact Details -></a><br><br>
        <a href="/pinterests">Ενδιαφέροντα/Personal Interests -></a>
      </body>
    </html>
    """
@app.route("/education")
def education():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 22px; text-align: center; background-color: #CCC0C6;">
      <h1>Education</h1>
      <hr>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p>-> University of Crete<br>
      Bachelor of Science, Mathematics<br>
      2022-2026<br>
      Grade: 7.57/10<br><br><br><br><br>
      ->1st High School of Souda<br>
      Greek<br>
      2019-2022<br>
      Grade: 19.1/20
    </body>
  </html>
  """
@app.route("/pinterests")
def pinterest():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 22px; text-align: center; background-color: #CCC0C6;">
      <h1>Personal Interests</h1>
      <hr>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p>Chess:<br> I play chess since a very young age,not professionally, my elo rating is 1446 </p>
      <a href="https://ratings.fide.com/profile/25844814"target="_blank"> FIDE official site</a><br><br>
      <p>Sports:<br>I like sports, basketball,football,formula with good company,working out and new adventures are a part of me. out<br><br>
      Travelling:<br> Some big cities i have visited: Athens,Thessaloniki,Sofia,Bansko,London<br><br>
      Movies/Series(and many more...):<br> Star Wars, Breaking Bad, Blacklist, From, Sherlock, Dexter, Marvel<br><br>
      Books(of course a very small sample):<br> Death in the Clouds(Agatha Christie),How to kill a mockingbird(Harper Lee),The big adventure of mathematics(Michael Launay)
    </body>
  </html>
  """

@app.route("/communication")
def communication():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 24px; text-align: center; background-color: #CCC0C6;">
      <h1>Contact Details</h1>
      <hr>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p>Phone number: </p>
      <a href="tel:+306970264045" style="text-decoration: none; color: navy;">+30 697 026 4045</a></p>
      <p>E-mail: </p>
      <a href="mailto: emm.pyrovolakis@gmail.com" style="text-decoration: none; color: navy;">emm.pyrovolakis@gmail.com</a></p>
    </body>
  </html>
  """

@app.route("/profesionallinks")
def profesionallinks():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 24px; text-align: center; background-color: #CCC0C6;">
      <h1>Profesional Links</h1>
      <hr>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p> Linkedin profile</p>
      <a href="https://www.linkedin.com/in/emmanouil-pyrovolakis-6b59973b2" target="_blank" style="color: blue;font-size: 18px;">View Linkedin Profile</a> 
      <p> Upwork profile</p>
      <a href="https://www.upwork.com/freelancers/~01d6c46b28807dd948?mp_source=share" target="_blank" style="color: blue;font-size: 18px;">View Upwork Profile</a> 
    </body>
  </html>
  """
@app.route("/interests")
def interests():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 24px; text-align: center; background-color: #CCC0C6;">
      <h1>Interests</h1>
      <hr>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p style="font-size:20px"> Numerical Analysis | Python | Analytical Problem Solving<br>
          I am a Mathematics graduate with a strong foundation in Optimization, Numerical Algorithms, Linear Algebra, and Mathematical Analysis.
          I work with Python to implement algorithms, solve structured problems, and explore data analytically. My academic training has given me a rigorous approach to problem-solving and clean logical thinking.
          I am currently preparing for a Master's or reasearch in Data Science and Machine Learning and looking to apply my mathematical and programming skills to real-world projects.
          I am especially interested in:<br>
            • Data analysis tasks<br>
            • Algorithm implementation<br>
            • Mathematical modeling<br>
            • Research assistance<br>
            • Python scripting and automation<br>
          If you are looking for someone analytical, detail-oriented, and committed to delivering structured solutions, I would be glad to collaborate.</p>
    </body>
  </html>
  """

@app.route("/workexperience")
def workexperience():
  return"""
  <html>
    <body style = "font-family: Arial;font-size: 18px; text-align: center; background-color: #CCC0C6;">
      <h1>Work Experience</h1>
      <a href="/"> <- Πίσω στην Αρχική</a><br><br>
      <p>-> Mathematics Tutor<br>
      2024-2026<br>
      Experienced in teaching both high school and univeristy students, breaking down complex mathematical problems into clear, manageable steps. Skilled at adapting explanations to different learning styles and academic levels. Supportive and patient communicator, committed to ensuring full understanding by providing thorough and repeated clarification when needed<br><br><br>
      ->Head Waiter<br>
      2023-2025 (Seasonal)<br>
      Aktaion Resataurant<br>
      Led service operations during high-demand seasons in a fast paced enviroment.Cordinated team workflow and ensured efficient table management and customer satisfaction. Handled guest requests and resolved issues with professionalism and composure. Developed leadership, decision making and multitasking skills under pressure<br><br><br>
      -> Barista/Waiter<br>
      2021-2023 (Seasonal)<br>
      Delizia Gelato Italiano<br>
      Worked in high-demand peak tourist seasons from the outset, consistently delivering high quality customer service in fast-paced and competitive enviroments. Demonstrated adaptability, efficiency and professionalism while managing multiple tasks and maintaining strong attention to detail
    </body>
  </html>
  """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
