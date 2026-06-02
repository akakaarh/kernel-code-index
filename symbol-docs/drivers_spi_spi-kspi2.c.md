# drivers/spi/spi-kspi2.c

Subsystem: drivers/spi

## Functions (18)

### kspi2_calc_minimal_divider
- Return type: static u8
- Signature: kspi2_calc_minimal_divider(struct kspi2 * kspi,u32 max_speed_hz)
- Line: 116

### kspi2_init
- Return type: static void
- Signature: kspi2_init(struct kspi2 * kspi)
- Line: 330

### kspi2_inuse_lock
- Return type: static int
- Signature: kspi2_inuse_lock(struct kspi2 * kspi)
- Line: 64

### kspi2_inuse_unlock
- Return type: static void
- Signature: kspi2_inuse_unlock(struct kspi2 * kspi)
- Line: 92

### kspi2_prepare_hardware
- Return type: static int
- Signature: kspi2_prepare_hardware(struct spi_controller * host)
- Line: 98

### kspi2_prepare_message
- Return type: static int
- Signature: kspi2_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 245

### kspi2_probe
- Return type: static int
- Signature: kspi2_probe(struct auxiliary_device * auxdev,const struct auxiliary_device_id * id)
- Line: 338

### kspi2_process_transfer
- Return type: static int
- Signature: kspi2_process_transfer(struct kspi2 * kspi,struct spi_transfer * t)
- Line: 164

### kspi2_register_devices
- Return type: static int
- Signature: kspi2_register_devices(struct kspi2 * kspi)
- Line: 310

### kspi2_remove
- Return type: static void
- Signature: kspi2_remove(struct auxiliary_device * auxdev)
- Line: 408

### kspi2_set_cs
- Return type: static void
- Signature: kspi2_set_cs(struct spi_device * spi,bool enable)
- Line: 233

### kspi2_setup
- Return type: static int
- Signature: kspi2_setup(struct spi_device * spi)
- Line: 262

### kspi2_setup_transfer
- Return type: static int
- Signature: kspi2_setup_transfer(struct kspi2 * kspi,struct spi_device * spi,struct spi_transfer * t)
- Line: 186

### kspi2_transfer_one
- Return type: static int
- Signature: kspi2_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 213

### kspi2_txrx_byte
- Return type: static int
- Signature: kspi2_txrx_byte(struct kspi2 * kspi,u8 tx,u8 * rx)
- Line: 142

### kspi2_unprepare_hardware
- Return type: static int
- Signature: kspi2_unprepare_hardware(struct spi_controller * host)
- Line: 106

### kspi2_unregister_devices
- Return type: static void
- Signature: kspi2_unregister_devices(struct kspi2 * kspi)
- Line: 298

### kspi2_write_control_reg
- Return type: static void
- Signature: kspi2_write_control_reg(struct kspi2 * kspi,u8 val,u8 mask)
- Line: 133

## Structs (1)

### kspi2
- Line: 52
- Members:
  - auxdev: keba_spi_auxdev *
  - base: void __iomem *
  - host: spi_controller *
  - base_speed_hz: u32
  - control_shadow: u8
  - device: spi_device **
  - device_size: int

## Variables (2)

- static **kspi2_devtype_aux** : const struct auxiliary_device_id[] (line 415)
- static **kspi2_driver_aux** : auxiliary_driver (line 421)

## Macros (28)

- **KSPI2** (line 12)
- **KSPI2_CLK_FREQ_100M** (line 20)
- **KSPI2_CLK_FREQ_125M** (line 18)
- **KSPI2_CLK_FREQ_33_3M** (line 17)
- **KSPI2_CLK_FREQ_50M** (line 19)
- **KSPI2_CLK_FREQ_62_5M** (line 16)
- **KSPI2_CLK_FREQ_MASK** (line 15)
- **KSPI2_CLK_FREQ_REG** (line 14)
- **KSPI2_CONTROL_CLK_DIV_MASK** (line 24)
- **KSPI2_CONTROL_CLK_DIV_MAX** (line 23)
- **KSPI2_CONTROL_CLK_MODE_MASK** (line 27)
- **KSPI2_CONTROL_CPHA** (line 25)
- **KSPI2_CONTROL_CPOL** (line 26)
- **KSPI2_CONTROL_INIT** (line 28)
- **KSPI2_CONTROL_REG** (line 22)
- **KSPI2_CS_NR_NONE** (line 37)
- **KSPI2_CS_NR_REG** (line 36)
- **KSPI2_DATA_REG** (line 34)
- **KSPI2_INUSE_SLEEP_US** (line 49)
- **KSPI2_INUSE_TIMEOUT_US** (line 50)
- **KSPI2_MODE_BITS** (line 39)
- **KSPI2_NUM_CS** (line 40)
- **KSPI2_SPEED_HZ_MAX**(kspi) (line 43)
- **KSPI2_SPEED_HZ_MIN**(kspi) (line 42)
- **KSPI2_STATUS_BUSY** (line 32)
- **KSPI2_STATUS_IN_USE** (line 31)
- **KSPI2_STATUS_REG** (line 30)
- **KSPI2_XFER_TIMEOUT_US**(kspi) (line 46)
