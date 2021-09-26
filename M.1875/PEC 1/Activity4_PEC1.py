# Please use Python 3 version

import sys
# import SHA-256 hash function library

# Expected Merkle roots
test_expected_merkle_root = 'b113d8475b3a318ef80db74b16e94bdeafdffdbff28eeec4161289689b15168b'
ex_expected_merkle_root = '6dbba50b72ad0569c2449090a371516e3865840e905483cac0f54d96944eee28'

# Block 117,000 transactions (hex format)
test_Transactions = [
    '120bcc99d9589ea3f0e44aafa19be787147036e3fdd9805a2eac318174494bf1'
    '52d5453fbfbb581de7cb5562e155def7c3f07cbe66bbb8df76f1a6d2aa5ec36a'
    'a1fe6fab72dad5b37d8b7f554853e887e575322c6a37a784d0144b5ab7b429b0'
    '6debe0e3c42a253b2b0ba67e1fb9bcfe57648574be004befbfe4b0a63795929a'
    '78baa3bc5bfad51731e20adbecc4f978454eb7ec11181b6255918adc1f94d958'
]

# Block 120,000 transactions (hex format)
ex_Transactions = [
    '1829755bdbe84f5a1ca579c1ed2f78a051a817b66ed4dfff35704cd6d4d644f9'
    'db6d13b57fb0daef6ebb8af735a4b2776f11143e760d0c90e4251613bb00e43b'
    '1824bac57c0ba9565e867a4915906a9c78c83ba3f668d0164bb0c4c9acb34fac'
    'a7ee0da5061982cb9c2bb95da715a90c3f8a717fa6d2f74a9934825017acaea6'
    '79b8ea58d3a3d18b583ac7b8fed5b7b06706a5198d4ffc38095d9fc55dc62030'
    'ba716aaf87bc2030bdc1a3ee7deadf34d36e8fa02cb848e73eabedd3e6a7d74b'
    'dedabaa2b1e6e5fff513bf0a2aeebccf2b650617ff540e4baa27ff3588692acc'
    '6182f42ea89a59df3a417f958e1c9bb3f0ea8ee7193cda760b477c4ce09c357c'
    '8469c30ba524b81509db66d1729bb2ee470329de6f3174f11ea7b86a4158b5d6'
    '1ecc492e27064d4d6ddf428376135f3fabdc1d8816e1b1655d28d82fe9e3c13d'
    '5bb631bfd9a819e9d4ee6188c624dd3d975970fb4d1ffdeb62dd39b92dd526a6'
    '875b82878572987f448f122bbe1f2235afa7eeab128619321221e703d99e4368'
    'ca744b08ea45c22d2951c25c48298b751c7caf6eea2c799054d484606d7a7f13'
    'c0cbad983ca538c242134c086b652f4ca068a89294dd68aab9c1d9de72e58653'
    'd81a57980bfcec9989e34f85d4c1e8905b940ea0d13949242a2de720d0b5b592'
    '3acd6221d34327217c06162cdf9ee133b47e7efe92e7b55361c96904faee0c6c'
    '0132cff762fbeb15d7d1421264c412401adda2a53a8fe173321aacdb37e5b7b0'
    '356e6a86dd145d2feb54cdef948de9ae23092469d5e9632abff6f81ad22c02e0'
    'cb7b6ef9ed762549cfcebf17076a22a726683ebbcf37e5a3fb678b45dc3b51db'
    '453369ba6418d0dfe687abec6f47e60244b4b76dacb844e53051c5944195227b'
    '77a0b8913236a39bc5f5e585efa893cd39e426ec1e766121becccecc4f49af39'
    '80808e54b8fd5391c88b5e5db8167516555a993bb4a7ddbe868e1854db9b4b02'
    '162cb86244da265330a264341ece720edc425eafe90efbc18258c4f1764b7076'
    '8f29c46680afd7d6e55fa46e3b1fcf00605c2640ff1e1cec7ba5441191054c36'
    '409be0865675eb7c3078401c994ea6a4c6c138b4e87ed53c73e9d0e71dee4598'
    '3420b2c059781f5ee772836b5207860ccf5f958a2c045161270f11eaf004c335'
    '5fb7b81731b7a0cfbe30f17b0a8c4844f6c48ce80a10d86e7110b0d820470e07'
    '09d79e6249a7233621a4f0889fe72898d730456ebae7854658faeb16d596fef2'
    '31f429a9b22ab93ab4548ab3b9b245f1e9e09407d66cb397244e07fa337264e7'
    '43d2584065ccb69a0b8b6f1f41544d07dea07411ba1fd25b456d49ce687bbacb'
    '3bad7fd1ca33664a96ed20c308683d82e6dfb8b12be3be5f6f61f438b6ce912b'
    'd619da0cd8aa21e1b33a7bcaf1e5ede1906308992ae5ffb41a02d16953b7ca2c'
    'c8c2bd8367dce6305d974c59741f8383833c1908cf27e18b614bd2b2e2517a8b'
    'ab1584e050d81da5565e93f40e6c5058079da429522471179e4de0fa5cf9611c'
    'fe8b4de4caca2fb8910194a34d0b6b8d3a08e518febe276f2a1646c6985828a8'
    '259d1dd303f1bcc8c40128596073cdcf243fb7af2d62ad36525dc49d5f913008'
    '6e78164bdb78b66616b70ba38e0916422f34c6316ade1ed39d795f04840bbdab'
    'c2d3aca99b1ca6c50494b8f90632a14c0c4ed9138f0c1fd7bf5084368eb86ced'
    '5c463283e2deeb1eccdf143d970c40dd117bfd85ad3f2e38ea3fdbca8e3198c3'
    'be26ca600b2566d20ccf59b3808ce283619902268407e5599802b5d4d8f52f0f'
    '6997dfd7f7f288a1ba7989b13a225f575316bbe9beb2dab91ce52a63324c6154'
    '57a14b64ea112d3cfc86395a19aff5267a1686d70c3726170b50ad218c7bfb0c'
    '5df91dea542064a69b1495e1899f84255dcbd50394a3b10602b70b1a27ef8a35'
    '76582f0ca5f93e2051a25a509d06155ebc7f46b87bfbe5b77db649cb02cc968e'
    '8d60c324946d620a794e89438c703c927af7da1184d0767709fc52846399d14c'
    '2e7a15f604e78871c621d737c3e9655363424ce9e85579b97eb420009a58d4f0'
    '854e1717d5d5f063367aee1345da0a4824d34c1c4456106c4dddd1c0265bf95a'
    'd2cedcae4b336b9daf5ffd050ad3895eaeb3a90f6fc87130eab7b583ad3c2bdd'
    '1adce1ebeb39c6f9a3b2c8ac5189f161d987217720c44ed81b10c3f1471e7438'
    '2e1aaa51b0433b83c65e7269b830675ad6a59f795ceb1b5ecbbd80af15c8b557'
    'fdfcbed87364ac3ffda6ff5eced6f2e39cb4d3d3dee42f18056b06bfac0c0cc9'
    '840ae018fd594b5e5927451c98d73d033651303ad00c4ef8f8546f9a33ab7415'
    '64ed1e2b01458624e74225e18deba497f4a122334ae03a77b980c98ca794aa8a'
    '42aed02a99f2dfa3cb32d64933bc569c127f352f29bd26a06e292dbeabd74119'
    'd7c9fa4b801a3a4ef78613f4c00707fbb5fea339a7a650bdcfdc11c749e8773e'
    '6a9fa4566fd2454f73daf71005c9f2ddb75e1c0ced2bcab89472583d60d92a4b'
]

# Function - Convert transactions from big endian into little endian (hex)
def big_endian_to_little_endian(transaction):
    _ = bytearray.fromhex(transaction)
    _.reverse()
    __ = ''.join(format(v, '02x') for v in _)
    
    return(__)

# Function - Calculate Merkle root
def merkle_root_func(transactions_set):
    # CODE HERE
    # use the function big_endian_to_little_endian(...)
    # merkle_root = ...
    # return merkle_root

# DO NOT MODIFY THIS FUNCTION
# Test merkle_root_func(...) function
def check_merkle_root():
    value = True
    while value:
        value = input(
            "Please select an option number:\n"
            "- Option 0: Exit.\n"
            "- Option 1: Use transactions from block 117,000 (5 transactions).\n"
            "- Option 2: Use transactions from block 120,000 (56 transactions).\n"
        )

        if(value == '0'):
            sys.exit("Bye!")

        elif(value == '1'):
            print(f'Checking calculated Merkle root against the expected value')

            merkle_root = merkle_root_func(test_Transactions)

            if test_expected_merkle_root == merkle_root:
                sys.exit('Well done, Merkle root values match!')
            else:
                sys.exit("Check your function, Merkle root values ​​do not match!")

        elif(value == '2'):
            print(f'Checking calculated Merkle root against the expected value')

            merkle_root = merkle_root_func(ex_Transactions)

            if ex_expected_merkle_root == merkle_root:
                sys.exit('Well done, Merkle root values match!')
            else:
                sys.exit("Check your function, Merkle root values ​​do not match!")

        else:
            print("Invalid option!\n")

check_merkle_root()
