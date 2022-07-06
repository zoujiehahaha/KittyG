import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
try:
    cred = credential.Credential("AKIDUpxrZ3IK9k7HCsITP5WheLnzwe7KI1Xo", "5wXt0sUryub3FCuMZWEgtqZ3IH1Lo46t")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    req = models.SentimentAnalysisRequest()
    params = {
        "Text": "爽死了"
    }
    req.from_json_string(json.dumps(params))

    resp = client.SentimentAnalysis(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)