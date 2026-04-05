resource "google_compute_address" "pasta_ip" {
  name   = "pasta-static-ip"
  region = "us-central1"
}

resource "google_compute_firewall" "allow_http_ssh" {
  name    = "allow-http-ssh"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["22", "80", "443"]
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
    access_config {
      nat_ip = google_compute_address.pasta_ip.addres
    }
  }

  metadata = {
    ssh-keys = "ubuntu:${file("C:/Users/Lagia/.ssh/id_ed25519_pasta.pub")}"
  }

  tags = ["http-server", "ssh"]
}