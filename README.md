Steps to Run in Terminal:

Update and Upgrade System: Before running the script, you may want to ensure that your system is fully updated:

    sudo apt-get update

    sudo apt-get upgrade -y

Install Required Packages Manually: Run these commands to install the tools in the install_commands list manually:

    sudo apt-get install net-tools dnsutils sslscan fierce network-manager resolvconf dnsmasq ssh iptables curl bleachbit privoxy tor macchanger finalrecon theharvester dnsenum dnsrecon wpscan nmap whatweb metagoofil

Running the Script: After installing the necessary dependencies, you can run the script:

Save the script as a .py file, e.g., dox_anyone.py.
    
Run the script using Python:

    python3 scanner.py

Check Output: The results will be written to a file called scanresults.txt in the same directory.

Build the Docker Image:

Navigate to the directory where your Dockerfile and dox_anyone.py are located.

Build the Docker image:

    docker build -t dox_anyone-image .

Run the Docker Container:

After the image is built, run it with:

    docker run --name dox_anyone-container dox_anyone-image

Check the Output:

You can access the container's output by checking the logs:

    docker logs dox_anyone-container

Alternatively, you can mount a local directory to store the scanresults.txt file outside the container:

    docker run -v /path/to/local/directory:/usr/src/app --name scanner-container scanner-image

This will mount the local directory /path/to/local/directory to /usr/src/app inside the container, allowing you to access the scanresults.txt file outside of the container.




