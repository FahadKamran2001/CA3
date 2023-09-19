from flask import Flask, render_template
import docker
app = Flask(__name__)
@app.route("/")
def index():
    # Get the Docker client
    client = docker.from_env()
    # Get the GitHub repository name
    repo_name = "CA3"
    # Pull the latest image from GitHub
    client.images.pull(repo_name)
    # Create a container from the image
    container = client.containers.create(repo_name)
    # Start the container
    container.start()
    # Get the container's IP address
    ip_address = container.attrs['NetworkSettings']['IPAddress']
    # Render the template with the IP address
    return render_template("index.html", ip_address=ip_address)
if __name__ == "__main__":
    app.run()