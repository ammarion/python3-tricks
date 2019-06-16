from src.ec2.vpc import VPC
from src.client_locator import EC2Client


def main():
    # Create a VPC
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print(f"VPC created: {vpc_response}")

    # Add name tag to VPC
    vpc_name = 'Boto3-VPC'
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)

    print(f"Added {vpc_name} to {vpc_id}")


if __name__ == '__main__':
    main()
