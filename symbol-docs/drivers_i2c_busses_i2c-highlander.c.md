# drivers/i2c/busses/i2c-highlander.c

Subsystem: drivers/i2c

## Functions (20)

### highlander_i2c_command
- Return type: static void
- Signature: highlander_i2c_command(struct highlander_i2c_dev * dev,u8 command,int len)
- Line: 111

### highlander_i2c_done
- Return type: static void
- Signature: highlander_i2c_done(struct highlander_i2c_dev * dev)
- Line: 69

### highlander_i2c_func
- Return type: static u32
- Signature: highlander_i2c_func(struct i2c_adapter * adapter)
- Line: 345

### highlander_i2c_irq
- Return type: static irqreturn_t
- Signature: highlander_i2c_irq(int irq,void * dev_id)
- Line: 160

### highlander_i2c_irq_disable
- Return type: static void
- Signature: highlander_i2c_irq_disable(struct highlander_i2c_dev * dev)
- Line: 59

### highlander_i2c_irq_enable
- Return type: static void
- Signature: highlander_i2c_irq_enable(struct highlander_i2c_dev * dev)
- Line: 54

### highlander_i2c_poll
- Return type: static void
- Signature: highlander_i2c_poll(struct highlander_i2c_dev * dev)
- Line: 170

### highlander_i2c_probe
- Return type: static int
- Signature: highlander_i2c_probe(struct platform_device * pdev)
- Line: 355

### highlander_i2c_read
- Return type: static int
- Signature: highlander_i2c_read(struct highlander_i2c_dev * dev)
- Line: 209

### highlander_i2c_remove
- Return type: static void
- Signature: highlander_i2c_remove(struct platform_device * pdev)
- Line: 438

### highlander_i2c_reset
- Return type: static int
- Signature: highlander_i2c_reset(struct highlander_i2c_dev * dev)
- Line: 142

### highlander_i2c_setup
- Return type: static void
- Signature: highlander_i2c_setup(struct highlander_i2c_dev * dev)
- Line: 74

### highlander_i2c_smbus_xfer
- Return type: static int
- Signature: highlander_i2c_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 275

### highlander_i2c_start
- Return type: static void
- Signature: highlander_i2c_start(struct highlander_i2c_dev * dev)
- Line: 64

### highlander_i2c_wait_for_ack
- Return type: static int
- Signature: highlander_i2c_wait_for_ack(struct highlander_i2c_dev * dev)
- Line: 148

### highlander_i2c_wait_for_bbsy
- Return type: static int
- Signature: highlander_i2c_wait_for_bbsy(struct highlander_i2c_dev * dev)
- Line: 125

### highlander_i2c_wait_xfer_done
- Return type: static int
- Signature: highlander_i2c_wait_xfer_done(struct highlander_i2c_dev * dev)
- Line: 197

### highlander_i2c_write
- Return type: static int
- Signature: highlander_i2c_write(struct highlander_i2c_dev * dev)
- Line: 254

### smbus_read_data
- Return type: static void
- Signature: smbus_read_data(u16 * src,u8 * dst,int len)
- Line: 100

### smbus_write_data
- Return type: static void
- Signature: smbus_write_data(u8 * src,u16 * dst,int len)
- Line: 89

## Structs (1)

### highlander_i2c_dev
- Line: 40
- Members:
  - dev: device *
  - base: void __iomem *
  - adapter: i2c_adapter
  - cmd_complete: completion
  - last_read_time: unsigned long
  - irq: int
  - buf: u8 *
  - buf_len: size_t

## Variables (6)

- static **highlander_i2c_algo** : const struct i2c_algorithm (line 350)
- static **highlander_i2c_driver** : platform_driver (line 451)
- static **iic_force_normal** : bool (line 51)
- static **iic_force_poll** : bool (line 51)
- static **iic_read_delay** : int (line 52)
- static **iic_timeout** : int (line 52)

## Macros (16)

- **SMCR** (line 20)
- **SMCR_ACKE** (line 24)
- **SMCR_BBSY** (line 23)
- **SMCR_IEIC** (line 26)
- **SMCR_IRIC** (line 22)
- **SMCR_RST** (line 25)
- **SMCR_START** (line 21)
- **SMMR** (line 30)
- **SMMR_CAP** (line 33)
- **SMMR_MODE0** (line 31)
- **SMMR_MODE1** (line 32)
- **SMMR_SP** (line 35)
- **SMMR_TMMD** (line 34)
- **SMSADR** (line 37)
- **SMSMADR** (line 28)
- **SMTRDR** (line 38)
