# drivers/i2c/busses/i2c-at91-core.c

Subsystem: drivers/i2c

## Functions (15)

### at91_disable_twi_interrupts
- Return type: void
- Signature: at91_disable_twi_interrupts(struct at91_twi_dev * dev)
- Line: 38

### at91_init_twi_bus
- Return type: void
- Signature: at91_init_twi_bus(struct at91_twi_dev * dev)
- Line: 54

### at91_twi_exit
- Return type: static void __exit
- Signature: at91_twi_exit(void)
- Line: 346

### at91_twi_get_driver_data
- Return type: static at91_twi_pdata *
- Signature: at91_twi_get_driver_data(struct platform_device * pdev)
- Line: 183

### at91_twi_init
- Return type: static int __init
- Signature: at91_twi_init(void)
- Line: 341

### at91_twi_irq_restore
- Return type: void
- Signature: at91_twi_irq_restore(struct at91_twi_dev * dev)
- Line: 49

### at91_twi_irq_save
- Return type: void
- Signature: at91_twi_irq_save(struct at91_twi_dev * dev)
- Line: 43

### at91_twi_probe
- Return type: static int
- Signature: at91_twi_probe(struct platform_device * pdev)
- Line: 196

### at91_twi_read
- Return type: unsigned
- Signature: at91_twi_read(struct at91_twi_dev * dev,unsigned reg)
- Line: 28

### at91_twi_remove
- Return type: static void
- Signature: at91_twi_remove(struct platform_device * pdev)
- Line: 267

### at91_twi_resume_noirq
- Return type: static int __maybe_unused
- Signature: at91_twi_resume_noirq(struct device * dev)
- Line: 305

### at91_twi_runtime_resume
- Return type: static int __maybe_unused
- Signature: at91_twi_runtime_resume(struct device * dev)
- Line: 288

### at91_twi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: at91_twi_runtime_suspend(struct device * dev)
- Line: 277

### at91_twi_suspend_noirq
- Return type: static int __maybe_unused
- Signature: at91_twi_suspend_noirq(struct device * dev)
- Line: 297

### at91_twi_write
- Return type: void
- Signature: at91_twi_write(struct at91_twi_dev * dev,unsigned reg,unsigned val)
- Line: 33

## Variables (13)

- static **at91_twi_devtypes** : const struct platform_device_id[] (line 90)
- static **at91_twi_driver** : platform_driver (line 330)
- static **at91_twi_pm** : const struct dev_pm_ops __maybe_unused (line 323)
- static **at91rm9200_config** : at91_twi_pdata (line 64)
- static **at91sam9260_config** : at91_twi_pdata (line 75)
- static **at91sam9261_config** : at91_twi_pdata (line 70)
- static **at91sam9g10_config** : at91_twi_pdata (line 85)
- static **at91sam9g20_config** : at91_twi_pdata (line 80)
- static **at91sam9x5_config** : at91_twi_pdata (line 112)
- static **atmel_twi_dt_ids** : const struct of_device_id[] (line 148)
- static **sam9x60_config** : at91_twi_pdata (line 136)
- static **sama5d2_config** : at91_twi_pdata (line 124)
- static **sama5d4_config** : at91_twi_pdata (line 117)
