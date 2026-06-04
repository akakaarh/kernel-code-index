# drivers/mmc/core/bus.c

Subsystem: drivers/mmc

## Functions (17)

### mmc_add_card
- Return type: int
- Signature: mmc_add_card(struct mmc_card * card)
- Line: 301

### mmc_alloc_card
- Return type: mmc_card *
- Signature: mmc_alloc_card(struct mmc_host * host,const struct device_type * type)
- Line: 278

### mmc_bus_probe
- Return type: static int
- Signature: mmc_bus_probe(struct device * dev)
- Line: 127

### mmc_bus_remove
- Return type: static void
- Signature: mmc_bus_remove(struct device * dev)
- Line: 135

### mmc_bus_resume
- Return type: static int
- Signature: mmc_bus_resume(struct device * dev)
- Line: 181

### mmc_bus_shutdown
- Return type: static void
- Signature: mmc_bus_shutdown(struct device * dev)
- Line: 143

### mmc_bus_suspend
- Return type: static int
- Signature: mmc_bus_suspend(struct device * dev)
- Line: 164

### mmc_bus_uevent
- Return type: static int
- Signature: mmc_bus_uevent(const struct device * dev,struct kobj_uevent_env * env)
- Line: 59

### mmc_register_bus
- Return type: int
- Signature: mmc_register_bus(void)
- Line: 230

### mmc_register_driver
- Return type: int
- Signature: mmc_register_driver(struct mmc_driver * drv)
- Line: 244

### mmc_release_card
- Return type: static void
- Signature: mmc_release_card(struct device * dev)
- Line: 264

### mmc_remove_card
- Return type: void
- Signature: mmc_remove_card(struct mmc_card * card)
- Line: 402

### mmc_runtime_resume
- Return type: static int
- Signature: mmc_runtime_resume(struct device * dev)
- Line: 206

### mmc_runtime_suspend
- Return type: static int
- Signature: mmc_runtime_suspend(struct device * dev)
- Line: 198

### mmc_unregister_bus
- Return type: void
- Signature: mmc_unregister_bus(void)
- Line: 235

### mmc_unregister_driver
- Return type: void
- Signature: mmc_unregister_driver(struct mmc_driver * drv)
- Line: 256

### type_show
- Return type: static ssize_t
- Signature: type_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 32

## Variables (3)

- static **mmc_bus_pm_ops** : const struct dev_pm_ops (line 215)
- static **mmc_bus_type** : const struct bus_type (line 220)
- static **mmc_dev_attrs** : attribute * [] (line 52)

## Macros (1)

- **to_mmc_driver**(d) (line 30)
