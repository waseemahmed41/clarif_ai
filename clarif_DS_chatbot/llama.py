from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

# Constants
PAT = 'your_pat_id_here'  # Replace with your actual PAT
USER_ID = 'deepseek-ai'
APP_ID = 'deepseek-chat'
MODEL_ID = 'your _model_id_here'  # Replace with your actual model ID
MODEL_VERSION_ID = 'your_model_version_id_here'  # Replace with your actual model version ID

# Init channel and stub once
channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)
metadata = (('authorization', 'Key ' + PAT),)
userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)


def get_response(prompt):
    """Gets response from Clarifai's DeepSeek model and returns it."""
    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject, 
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(raw=prompt)
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    # Extract and return the output text
    output = post_model_outputs_response.outputs[0]
    return output.data.text.raw
