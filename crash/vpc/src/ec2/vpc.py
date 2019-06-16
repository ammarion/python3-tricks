
class VPC:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

    def create_vpc(self):
        """Create a new VPC."""
        print('Creating a VPC........')
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16'
        )

    def add_name_tag(self, resource_id, resource_name):
        print(f"Adding {resource_name} tag to the {resource_id}")
        return self._client.create_tags(
            Resources=[resource_id],
            Tags=[{
                'Key': 'Name',
                'Value': 'resource_name'
            }]
        )

