# solmon
Generate keypair:
```
python program/generate_keypair.py
```

Initialize:
```
python -m program --wallet wallet-keypair.json --idl program/idl.json initialize <keypair-file> 2
```

Run solmon:
```
python -m solmon program/idl.json GXV2cYjG8ECRermN9f6X2zpsQsRqF34BEMNjGWGEqkCi <account-public-key> NewAccount data lt 5
```

Modify data:
```
python -m program --wallet wallet-keypair.json --idl program/idl.json modify_data <account-public-key> 6
```

After 30s a warning will be displayed that the condition `NewAccount.data < 5` was violated.