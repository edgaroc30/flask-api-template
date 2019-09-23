Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  # config.disksize.size = '50GB'
  config.vm.provider "virtualbox" do |vb|
    vb.name = "flask-api"
    # Limit the memory for this VM
    vb.memory = "8192"
    # Limit the number of CPUs available for this VM
    vb.customize ["modifyvm", :id, "--cpus", 2]
    # Limit the CPU usage for this VM in the host
    vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
  end

  # Port mapping

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 22, host: 22
  config.vm.network "forwarded_port", guest: 443, host: 443
  config.vm.network "forwarded_port", guest: 3306, host: 3306
  config.vm.network "public_network", type: "dhcp"

  # Mariadb for general development
  config.vm.provision "docker" do |d|
    d.build_image "/vagrant/app",
      args: "-t flask-api:latest"
    d.run "flask-api:latest",
      args: "--detach \
      --name flask-api \
      --publish 80:5000"
    d.run "mariadb/server:10.3",
      # cmd: "bash -l",
      args: "--detach  \
      --publish 3306:3306 \
      -e MYSQL_ROOT_PASSWORD=mariadbroot \
      --name mariadb \
      --restart always \
      --volume /srv/mariadb/mysql:/var/lib/mysql \
      --memory='1GB'"
  end


  config.vm.provision "file", source: "./provision/.bash_profile", destination: "$HOME"
  config.vm.provision :shell, path: "./provision/bootstrap.sh"

end