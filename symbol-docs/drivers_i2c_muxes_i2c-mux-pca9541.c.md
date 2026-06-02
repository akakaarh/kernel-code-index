# drivers/i2c/muxes/i2c-mux-pca9541.c

Subsystem: drivers/i2c

## Functions (8)

### pca9541_arbitrate
- Return type: static int
- Signature: pca9541_arbitrate(struct i2c_client * client)
- Line: 174

### pca9541_probe
- Return type: static int
- Signature: pca9541_probe(struct i2c_client * client)
- Line: 286

### pca9541_reg_read
- Return type: static int
- Signature: pca9541_reg_read(struct i2c_client * client,u8 command)
- Line: 109

### pca9541_reg_write
- Return type: static int
- Signature: pca9541_reg_write(struct i2c_client * client,u8 command,u8 val)
- Line: 95

### pca9541_release_bus
- Return type: static void
- Signature: pca9541_release_bus(struct i2c_client * client)
- Line: 127

### pca9541_release_chan
- Return type: static int
- Signature: pca9541_release_chan(struct i2c_mux_core * muxc,u32 chan)
- Line: 274

### pca9541_remove
- Return type: static void
- Signature: pca9541_remove(struct i2c_client * client)
- Line: 327

### pca9541_select_chan
- Return type: static int
- Signature: pca9541_select_chan(struct i2c_mux_core * muxc,u32 chan)
- Line: 248

## Structs (1)

### pca9541
- Line: 70
- Members:
  - client: i2c_client *
  - select_timeout: unsigned long
  - arb_timeout: unsigned long

## Variables (4)

- static **pca9541_control** : const u8[16] (line 162)
- static **pca9541_driver** : i2c_driver (line 334)
- static **pca9541_id** : const struct i2c_device_id[] (line 76)
- static **pca9541_of_match** : const struct of_device_id[] (line 84)

## Macros (21)

- **BUSON** (line 61)
- **MYBUS** (line 62)
- **PCA9541_CONTROL** (line 43)
- **PCA9541_CTL_BUSINIT** (line 50)
- **PCA9541_CTL_BUSON** (line 48)
- **PCA9541_CTL_MYBUS** (line 46)
- **PCA9541_CTL_NBUSON** (line 49)
- **PCA9541_CTL_NMYBUS** (line 47)
- **PCA9541_CTL_NTESTON** (line 52)
- **PCA9541_CTL_TESTON** (line 51)
- **PCA9541_ISTAT** (line 44)
- **PCA9541_ISTAT_BUSINIT** (line 55)
- **PCA9541_ISTAT_BUSLOST** (line 57)
- **PCA9541_ISTAT_BUSOK** (line 56)
- **PCA9541_ISTAT_INTIN** (line 54)
- **PCA9541_ISTAT_MYTEST** (line 58)
- **PCA9541_ISTAT_NMYTEST** (line 59)
- **SELECT_DELAY_LONG** (line 68)
- **SELECT_DELAY_SHORT** (line 67)
- **busoff**(x) (line 64)
- **mybus**(x) (line 63)
