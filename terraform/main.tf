resource "google_compute_firewall" "allow_http_ssh" {
  name    = "allow-http-ssh"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["22", "80"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_instance" "pasta-vm" {
  name         = "pasta-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "ubuntu:${file("C:/Users/Lagia/.ssh/id_ed25519_pasta.pub")}"
  }

  tags = ["http-server", "ssh"]
}