# ================================
# Création de la VM Pasta Web (Oracle Always Free - Paris)
# ================================

resource "oci_core_instance" "pasta_web_server" {
  availability_domain = var.availability_domain
  compartment_id      = var.compartment_id
  display_name        = "pasta-web-server"
  shape               = "VM.Standard.A1.Flex"

  shape_config {
    ocpus         = 2
    memory_in_gbs = 12
  }

  # Configuration réseau
  create_vnic_details {
    subnet_id        = var.subnet_id
    assign_public_ip = true
  }

  # Image Ubuntu ARM
  source_details {
    source_type = "image"
    source_id   = var.image_id        # C'est ici qu'on met l'image (et non image_id en top level)
  }

  # Clé SSH
  metadata = {
    ssh_authorized_keys = file(var.ssh_public_key_path)
  }

  # Tags (utilise freeform_tags au lieu de tags)
  freeform_tags = {
    Name = "pasta-web"
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