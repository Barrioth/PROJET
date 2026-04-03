variable "tenancy_ocid" {
  type        = string
}

variable "user_ocid" {
  type        = string
}

variable "fingerprint" {
  type        = string
}

variable "private_key_path" {
  type        = string
}

variable "compartment_id" {
  type        = string
}

variable "ssh_public_key_path" {
  type        = string
}

variable "subnet_id" {
  type        = string
}

variable "availability_domain" {
  type    = string
  default = "eu-paris-1-AD-1"
}

variable "image_id" {
  type    = string
  default = "ocid1.image.oc1.eu-paris-1.aaaaaaaaxoifps32ako2src2klbta4b2aizme544u5z2w7v42pp4hqiyjz7q"
}