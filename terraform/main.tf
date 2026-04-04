# ================================
# Création de la VM Pasta Web (OAF - Paris)
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
    subnet_id       = var.subnet_id
    assign_public_ip = true
  }

  source_details {
    source_type = "image"
    source_id   = var.image_id
  }

  metadata = {
    ssh_authorized_keys = file("~/.oci/id_rsa.pub")
  }

  freeform_tags = {
    Name    = "pasta-web"
    Project = "PROJET"
  }
}

# Outputs
output "public_ip" {
  value       = oci_core_instance.pasta_web_server.public_ip
  description = "IP publique de ton serveur"
}

output "ssh_command" {
  value       = "ssh ubuntu@${oci_core_instance.pasta_web_server.public_ip}"
  description = "Commande pour te connecter en SSH"
}