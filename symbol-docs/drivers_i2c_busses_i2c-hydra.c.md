# drivers/i2c/busses/i2c-hydra.c

Subsystem: drivers/i2c

## Functions (8)

### hydra_bit_getscl
- Return type: static int
- Signature: hydra_bit_getscl(void * data)
- Line: 68

### hydra_bit_getsda
- Return type: static int
- Signature: hydra_bit_getsda(void * data)
- Line: 73

### hydra_bit_setscl
- Return type: static void
- Signature: hydra_bit_setscl(void * data,int state)
- Line: 44

### hydra_bit_setsda
- Return type: static void
- Signature: hydra_bit_setsda(void * data,int state)
- Line: 56

### hydra_probe
- Return type: static int
- Signature: hydra_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 102

### hydra_remove
- Return type: static void
- Signature: hydra_remove(struct pci_dev * dev)
- Line: 129

### pdregr
- Return type: static u32
- Signature: pdregr(void * data)
- Line: 38

### pdregw
- Return type: static void
- Signature: pdregw(void * data,u32 val)
- Line: 32

## Variables (4)

- static **hydra_adap** : i2c_adapter (line 89)
- static **hydra_bit_data** : i2c_algo_bit_data (line 80)
- static **hydra_driver** : pci_driver (line 139)
- static **hydra_ids** : const struct pci_device_id[] (line 95)

## Macros (8)

- **HYDRA_CPD_PD0** (line 22)
- **HYDRA_CPD_PD1** (line 23)
- **HYDRA_CPD_PD2** (line 24)
- **HYDRA_CPD_PD3** (line 25)
- **HYDRA_SCLK** (line 27)
- **HYDRA_SCLK_OE** (line 29)
- **HYDRA_SDAT** (line 28)
- **HYDRA_SDAT_OE** (line 30)
