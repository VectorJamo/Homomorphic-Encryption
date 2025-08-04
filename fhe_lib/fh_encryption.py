import tenseal as ts
import torch
import utilities as util

# CONTEXT AND KEY GENERATION
def generate_fhe_context():
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )

    context.generate_galois_keys() # Create the public and private key pair
    context.global_scale = 2**40

    return context

def get_secret_context_serialized(context):
    return context.serialize(save_secret_key = True)

def get_public_context_serialized(context):
    context.make_context_public() 
    public_context = context.serialize()
    return public_context

# WRITE KEYS AND DATA
def save_secret_context_serialized(path, secret_context_serialized):
    util.write_data(path, secret_context_serialized)

def save_public_context_serialized(path, public_context_serialized):
    util.write_data(path, public_context_serialized)

def save_serialized_data(path, data_serialized):
    util.write_data(path, data_serialized)

# ENCRYPTION
def encrypt_flattened_vector(public_context, data):
    return ts.ckks_vector(public_context, data)

def encrypt_tensor(public_context, tensor):
    original_shape = tensor.shape
    flattened_tensor = tensor.flatten()
    
    tensor_encrypted = ts.ckks_vector(public_context, flattened_tensor)

    return tensor_encrypted, original_shape