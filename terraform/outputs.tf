#output "public_ip" {
#  value = google_compute_instance.pasta-vm.network_interface[0].access_config[0].nat_ip
#}
output "public_ip" {
  value = google_compute_address.pasta_ip.address
}