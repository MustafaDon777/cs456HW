terraform {
  backend "s3" {
    bucket = "terraform-state-djangoapp-ledgerpay-mustafadon777" 
    key    = "terraform.tfstate"
    region = "us-east-2" 
  }
}