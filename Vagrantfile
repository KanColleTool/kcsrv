# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/wily64"

  # Setup a host-only network on 10.1.1.4
  config.vm.network "private_network", ip: "10.1.1.4"

  config.vm.provider "virtualbox" do |vb|
    # Up the amount of memory used, as two gunicorns, psql, and another dev process can use a lot of memory.
     vb.memory = "1024"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
  end
end
