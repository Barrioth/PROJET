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
    ssh_authorized_keys = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPF7IUTXQUZVPY6oKLNZbF3INAumvGR7gyfE/38Sl0XTExJQH9GX9nwwP6eoesGKVHz7NNmiGVxk/ja0ZQX2Yc+mekAGdHBrKz977lrefORKwcRk741Hd5ayIEmF2topsm23s5/Yi7cB/LIVDYVAUreulZWa6FznyCueIX7GOlLJcvmSBj6Gm+7mB5+AjiRXvmd0FOpJtBO+eVl3Rzhfp1dv4iXa/7teO6WC01n4WxALKHtncGLdm+4CLnzDBK8r0v3ArKYN7moJzEKYHo/UrRtANpybNLi2bjCsiV77Uo9Kcen+BEP8G9tvB4/5v3//quMp+8YQD/VqBfAHT1zCuX"
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