import gdown

url = 'https://drive.google.com/uc?id=1oeSnkgJpwyudtTx-f5CE84B7e-Vkv3yK'
output = 'tensorflow-2.3.1-cp36-cp36m-linux_aarch64.whl'
gdown.download(url, output, quiet=False)
