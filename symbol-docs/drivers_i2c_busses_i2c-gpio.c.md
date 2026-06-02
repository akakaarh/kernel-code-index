# drivers/i2c/busses/i2c-gpio.c

Subsystem: drivers/i2c

## Functions (20)

### fops_incomplete_addr_phase_set
- Return type: static int
- Signature: fops_incomplete_addr_phase_set(void * data,u64 addr)
- Line: 129

### fops_incomplete_write_byte_set
- Return type: static int
- Signature: fops_incomplete_write_byte_set(void * data,u64 addr)
- Line: 146

### fops_inject_panic_set
- Return type: static int
- Signature: fops_inject_panic_set(void * data,u64 duration)
- Line: 239

### fops_lose_arbitration_set
- Return type: static int
- Signature: fops_lose_arbitration_set(void * data,u64 duration)
- Line: 210

### i2c_gpio_exit
- Return type: static void __exit
- Signature: i2c_gpio_exit(void)
- Line: 499

### i2c_gpio_fault_injector_init
- Return type: static void
- Signature: i2c_gpio_fault_injector_init(struct platform_device * pdev)
- Line: 275

### i2c_gpio_fault_injector_init
- Return type: static void
- Signature: i2c_gpio_fault_injector_init(struct platform_device * pdev)
- Line: 255

### i2c_gpio_fi_act_on_scl_irq
- Return type: static int
- Signature: i2c_gpio_fi_act_on_scl_irq(struct i2c_gpio_private_data * priv,irqreturn_t handler (int,void *))
- Line: 165

### i2c_gpio_get_desc
- Return type: static gpio_desc *
- Signature: i2c_gpio_get_desc(struct device * dev,const char * con_id,unsigned int index,enum gpiod_flags gflags)
- Line: 303

### i2c_gpio_get_properties
- Return type: static void
- Signature: i2c_gpio_get_properties(struct device * dev,struct i2c_gpio_platform_data * pdata)
- Line: 279

### i2c_gpio_getscl
- Return type: static int
- Signature: i2c_gpio_getscl(void * data)
- Line: 66

### i2c_gpio_getsda
- Return type: static int
- Signature: i2c_gpio_getsda(void * data)
- Line: 59

### i2c_gpio_incomplete_transfer
- Return type: static void
- Signature: i2c_gpio_incomplete_transfer(struct i2c_gpio_private_data * priv,u32 pattern,u8 pattern_size)
- Line: 104

### i2c_gpio_init
- Return type: static int __init
- Signature: i2c_gpio_init(void)
- Line: 487

### i2c_gpio_probe
- Return type: static int
- Signature: i2c_gpio_probe(struct platform_device * pdev)
- Line: 339

### i2c_gpio_remove
- Return type: static void
- Signature: i2c_gpio_remove(struct platform_device * pdev)
- Line: 453

### i2c_gpio_setscl_val
- Return type: static void
- Signature: i2c_gpio_setscl_val(void * data,int state)
- Line: 52

### i2c_gpio_setsda_val
- Return type: static void
- Signature: i2c_gpio_setsda_val(void * data,int state)
- Line: 39

### inject_panic_irq
- Return type: static irqreturn_t
- Signature: inject_panic_irq(int irq,void * dev_id)
- Line: 229

### lose_arbitration_irq
- Return type: static irqreturn_t
- Signature: lose_arbitration_irq(int irq,void * dev_id)
- Line: 197

## Structs (1)

### i2c_gpio_private_data
- Line: 21
- Members:
  - sda: gpio_desc *
  - scl: gpio_desc *
  - adap: i2c_adapter
  - bit_data: i2c_algo_bit_data
  - pdata: i2c_gpio_platform_data
  - scl_irq_completion: completion
  - scl_irq_data: u64

## Variables (3)

- static **i2c_gpio_acpi_match** : const struct acpi_device_id[] (line 471)
- static **i2c_gpio_driver** : platform_driver (line 477)
- static **i2c_gpio_dt_ids** : const struct of_device_id[] (line 464)

## Macros (5)

- **WIRE_ATTRIBUTE**(wire) (line 80)
- **getscl**(bd) (line 78)
- **getsda**(bd) (line 77)
- **setscl**(bd,val) (line 76)
- **setsda**(bd,val) (line 75)
