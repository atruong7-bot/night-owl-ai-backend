from flask import Flask, render_template

#__name__ tells flask this is the starting point of the application, look for resources relative to this file's location
#if __name__ is run directly, __name__ == "__main__
#if imported, __name == "filename" (app)
app = Flask(__name__) 


# #route decorator, when a user goes to the root url /, run the function below it
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say-hello')
def hello():
    return "Hello, World"
# #if the script is being run directly through this file, then allow for debugging 
if __name__ == "__main__":
    app.run(debug =True)