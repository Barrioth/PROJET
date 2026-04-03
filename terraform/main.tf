# ================================
# Création de la VM Pasta Web (Oracle Always Free - Paris)
# ================================

data "oci_identity_availability_domain" "ad" {
  compartment_id = var.compartment_id
  ad_number      = 1
}

resource "oci_core_instance" "pasta_web_server" {
  availability_domain = data.oci_identity_availability_domain.ad.name
  compartment_id      = var.compartment_id
  display_name        = "pasta-web-server"
  shape               = "VM.Standard.A1.Flex"

  shape_config {
    ocpus         = 1
    memory_in_gbs = 6
  }

  create_vnic_details {
    subnet_id        = var.subnet_id
    assign_public_ip = true
  }

  source_details {
    source_type = "image"
    source_id   = var.image_id
  }

  metadata = {
    ssh_authorized_keys = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3riGjl6ULQHiKWQYzrI4vUmPcPTCIyQlTzRAIHTck2tulRWpQPUkCDvegW4yN3rwNi2jQC63DZ5nRU+c9EbjnKqI2iYkVaKHrzMPHpAE+wgh2TAe+cQ3wgd2S59zsQCnRYjxteKs36cntQ6fTuJK0eVMc4MX3DowZck/gQCrTeNFL9h8JPSF6LRKYzm0zIrdMxBIJ5NwVoG80N6QVTeoOvU9yhtjUhYt3wF2jeLAQIiieWCo5LCEyvtxspL5kcaAXPS8JY8mG9RkmZhPMx0Ct80WuPEMCiT0W2ypmvvgdAEOpErcJkarOYT6LueS+MoFZbGLxDQv8Psn0KQG/WAl/QIDAQAB"
  }

  freeform_tags = {
    Name    = "pasta-web"
    Project = "PROJET"
  }
}

# Outputs très utiles
output "public_ip" {
  value       = oci_core_instance.pasta_web_server.public_ip
  description = "IP publique de ton serveur"
}

output "ssh_command" {
  value       = "ssh ubuntu@${oci_core_instance.pasta_web_server.public_ip}"
  description = "Commande pour te connecter en SSH"
}