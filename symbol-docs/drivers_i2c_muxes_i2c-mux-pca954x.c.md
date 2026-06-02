# drivers/i2c/muxes/i2c-mux-pca954x.c

Subsystem: drivers/i2c

## Functions (16)

### idle_state_show
- Return type: static ssize_t
- Signature: idle_state_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 359

### idle_state_store
- Return type: static ssize_t
- Signature: idle_state_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 370

### pca954x_cleanup
- Return type: static void
- Signature: pca954x_cleanup(struct i2c_mux_core * muxc)
- Line: 464

### pca954x_deselect_mux
- Return type: static int
- Signature: pca954x_deselect_mux(struct i2c_mux_core * muxc,u32 chan)
- Line: 336

### pca954x_get_reset
- Return type: static int
- Signature: pca954x_get_reset(struct device * dev,struct pca954x * data)
- Line: 524

### pca954x_init
- Return type: static int
- Signature: pca954x_init(struct i2c_client * client,struct pca954x * data)
- Line: 481

### pca954x_irq_handler
- Return type: static irqreturn_t
- Signature: pca954x_irq_handler(int irq,void * dev_id)
- Line: 405

### pca954x_irq_set_type
- Return type: static int
- Signature: pca954x_irq_set_type(struct irq_data * idata,unsigned int type)
- Line: 422

### pca954x_irq_setup
- Return type: static int
- Signature: pca954x_irq_setup(struct i2c_mux_core * muxc)
- Line: 434

### pca954x_probe
- Return type: static int
- Signature: pca954x_probe(struct i2c_client * client)
- Line: 556

### pca954x_reg_write
- Return type: static int
- Signature: pca954x_reg_write(struct i2c_adapter * adap,struct i2c_client * client,u8 val)
- Line: 300

### pca954x_regval
- Return type: static u8
- Signature: pca954x_regval(struct pca954x * data,u8 chan)
- Line: 310

### pca954x_remove
- Return type: static void
- Signature: pca954x_remove(struct i2c_client * client)
- Line: 677

### pca954x_reset_deassert
- Return type: static void
- Signature: pca954x_reset_deassert(struct pca954x * data)
- Line: 545

### pca954x_resume
- Return type: static int
- Signature: pca954x_resume(struct device * dev)
- Line: 686

### pca954x_select_chan
- Return type: static int
- Signature: pca954x_select_chan(struct i2c_mux_core * muxc,u32 chan)
- Line: 319

## Structs (2)

### chip_desc
- Line: 96
- Members:
  - nchans: u8
  - num_gpios: u8
  - regmap: regmap *
  - gpiochip: gpio_chip
  - chip: const struct chip_desc *
  - nchans: u8
  - enable: u8
  - has_irq: u8
  - muxtype: chip_desc::muxtype
  - id: i2c_device_identity
  - chip: const struct chip_desc *
  - last_chan: u8
  - idle_state: s32
  - client: i2c_client *
  - irq: irq_domain *
  - irq_mask: unsigned int
  - lock: raw_spinlock_t
  - supply: regulator *
  - reset_gpio: gpio_desc *
  - reset_cont: reset_control *

### pca954x
- Line: 107
- Members:
  - nchans: u8
  - enable: u8
  - has_irq: u8
  - muxtype: chip_desc::muxtype
  - id: i2c_device_identity
  - chip: const struct chip_desc *
  - last_chan: u8
  - idle_state: s32
  - client: i2c_client *
  - irq: irq_domain *
  - irq_mask: unsigned int
  - lock: raw_spinlock_t
  - supply: regulator *
  - reset_gpio: gpio_desc *
  - reset_cont: reset_control *

## Enums (2)

### muxtype
- Line: 100

### pca_type
- Line: 75

## Variables (5)

- static **chips** : const struct chip_desc[] (line 126)
- static **pca954x_driver** : i2c_driver (line 702)
- static **pca954x_id** : const struct i2c_device_id[] (line 252)
- static **pca954x_irq_chip** : irq_chip (line 429)
- static **pca954x_of_match** : const struct of_device_id[] (line 275)

## Macros (8)

- **MAX7357_CONF_DISCON_SINGLE_CHAN** (line 70)
- **MAX7357_CONF_FLUSH_OUT** (line 68)
- **MAX7357_CONF_INT_ENABLE** (line 67)
- **MAX7357_CONF_PRECONNECT_TEST** (line 71)
- **MAX7357_CONF_RELEASE_INT** (line 69)
- **MAX7357_POR_DEFAULT_CONF** (line 73)
- **PCA954X_IRQ_OFFSET** (line 59)
- **PCA954X_MAX_NCHANS** (line 57)
