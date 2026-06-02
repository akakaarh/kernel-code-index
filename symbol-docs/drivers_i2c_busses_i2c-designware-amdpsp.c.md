# drivers/i2c/busses/i2c-designware-amdpsp.c

Subsystem: drivers/i2c

## Functions (12)

### check_i2c_req_sts
- Return type: static int
- Signature: check_i2c_req_sts(struct psp_i2c_req * req)
- Line: 39

### i2c_adapter_dw_psp_lock_bus
- Return type: static void
- Signature: i2c_adapter_dw_psp_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 235

### i2c_adapter_dw_psp_trylock_bus
- Return type: static int
- Signature: i2c_adapter_dw_psp_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 242

### i2c_adapter_dw_psp_unlock_bus
- Return type: static void
- Signature: i2c_adapter_dw_psp_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 256

### i2c_dw_amdpsp_probe_lock_support
- Return type: int
- Signature: i2c_dw_amdpsp_probe_lock_support(struct dw_i2c_dev * dev)
- Line: 269

### psp_acquire_i2c_bus
- Return type: static int
- Signature: psp_acquire_i2c_bus(void)
- Line: 167

### psp_release_i2c_bus
- Return type: static void
- Signature: psp_release_i2c_bus(void)
- Line: 204

### psp_release_i2c_bus_deferred
- Return type: static void
- Signature: psp_release_i2c_bus_deferred(struct work_struct * work)
- Line: 152

### psp_send_i2c_req
- Return type: static int
- Signature: psp_send_i2c_req(enum psp_i2c_req_type i2c_req_type)
- Line: 89

### psp_send_i2c_req_cezanne
- Return type: static int
- Signature: psp_send_i2c_req_cezanne(struct psp_i2c_req * req)
- Line: 67

### psp_send_i2c_req_doorbell
- Return type: static int
- Signature: psp_send_i2c_req_doorbell(struct psp_i2c_req * req)
- Line: 78

### release_bus
- Return type: static void
- Signature: release_bus(void)
- Line: 135

## Structs (1)

### psp_i2c_req
- Line: 25
- Members:
  - hdr: psp_req_buffer_hdr
  - type: psp_i2c_req_type

## Enums (1)

### psp_i2c_req_type
- Line: 19

## Variables (6)

- static **_psp_send_i2c_req** : int (*)(struct psp_i2c_req * req) (line 36)
- static **i2c_dw_psp_lock_ops** : const struct i2c_lock_operations (line 263)
- static **psp_i2c_access_count** : u32 (line 32)
- static **psp_i2c_dev** : device * (line 34)
- static **psp_i2c_mbox_fail** : bool (line 33)
- static **psp_i2c_sem_acquired** : unsigned long (line 31)

## Macros (6)

- **PSP_I2C_REQ_RETRY_CNT** (line 13)
- **PSP_I2C_REQ_RETRY_DELAY_US** (line 14)
- **PSP_I2C_REQ_STS_BUS_BUSY** (line 16)
- **PSP_I2C_REQ_STS_INV_PARAM** (line 17)
- **PSP_I2C_REQ_STS_OK** (line 15)
- **PSP_I2C_RESERVATION_TIME_MS** (line 11)
