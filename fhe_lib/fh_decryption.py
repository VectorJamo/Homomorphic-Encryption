import tenseal as ts
import torch
import utilities as util

# LOAD KEYS AND DATA
def load_public_context_from_file(path):
    public_context = ts.context_from(util.read_data(path))
    return public_context

def load_secret_context_from_file(path):
    secret_context = ts.context_from(util.read_data(path))
    return secret_context

def load_data_serialized(path):
    data_serialized = util.read_data(path)
    return data_serialized

# DECRYPTION
def decrypt_flattened_vector(secret_context, data_encrypted):
    data_encrypted.link_context(secret_context)
    data_decrypted = data_encrypted.decrypt()
    return data_decrypted

def decrypt_tensor(secret_context, tensor_encrypted, original_shape):
    tensor_encrypted.link_context(secret_context)
    tensor_decrypted = tensor_encrypted.decrypt()

    # Reshaping the decrypted data into original tensor's shape
    tensor_final_decrypted = torch.tensor(tensor_decrypted, dtype=torch.float32).view(original_shape)
    return tensor_final_decrypted