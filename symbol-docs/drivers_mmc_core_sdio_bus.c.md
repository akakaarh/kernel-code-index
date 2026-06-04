# drivers/mmc/core/sdio_bus.c

Subsystem: drivers/mmc

## Functions (19)

### __sdio_register_driver
- Return type: int
- Signature: __sdio_register_driver(struct sdio_driver * drv,struct module * owner)
- Line: 287

### sdio_acpi_set_handle
- Return type: static void
- Signature: sdio_acpi_set_handle(struct sdio_func * func)
- Line: 380

### sdio_acpi_set_handle
- Return type: static void
- Signature: sdio_acpi_set_handle(struct sdio_func * func)
- Line: 372

### sdio_add_func
- Return type: int
- Signature: sdio_add_func(struct sdio_func * func)
- Line: 393

### sdio_alloc_func
- Return type: sdio_func *
- Signature: sdio_alloc_func(struct mmc_card * card)
- Line: 336

### sdio_bus_match
- Return type: static int
- Signature: sdio_bus_match(struct device * dev,const struct device_driver * drv)
- Line: 111

### sdio_bus_probe
- Return type: static int
- Signature: sdio_bus_probe(struct device * dev)
- Line: 153

### sdio_bus_remove
- Return type: static void
- Signature: sdio_bus_remove(struct device * dev)
- Line: 206

### sdio_bus_shutdown
- Return type: static void
- Signature: sdio_bus_shutdown(struct device * dev)
- Line: 235

### sdio_bus_uevent
- Return type: static int
- Signature: sdio_bus_uevent(const struct device * dev,struct kobj_uevent_env * env)
- Line: 123

### sdio_legacy_shutdown
- Return type: static void
- Signature: sdio_legacy_shutdown(struct sdio_func * func)
- Line: 274

### sdio_match_device
- Return type: static const struct sdio_device_id *
- Signature: sdio_match_device(struct sdio_func * func,const struct sdio_driver * sdrv)
- Line: 93

### sdio_match_one
- Return type: static const struct sdio_device_id *
- Signature: sdio_match_one(struct sdio_func * func,const struct sdio_device_id * id)
- Line: 81

### sdio_register_bus
- Return type: int
- Signature: sdio_register_bus(void)
- Line: 264

### sdio_release_func
- Return type: static void
- Signature: sdio_release_func(struct device * dev)
- Line: 315

### sdio_remove_func
- Return type: void
- Signature: sdio_remove_func(struct sdio_func * func)
- Line: 415

### sdio_set_of_node
- Return type: static void
- Signature: sdio_set_of_node(struct sdio_func * func)
- Line: 383

### sdio_unregister_bus
- Return type: void
- Signature: sdio_unregister_bus(void)
- Line: 269

### sdio_unregister_driver
- Return type: void
- Signature: sdio_unregister_driver(struct sdio_driver * drv)
- Line: 308

## Variables (3)

- static **sdio_bus_pm_ops** : const struct dev_pm_ops (line 244)
- static **sdio_bus_type** : const struct bus_type (line 253)
- static **sdio_dev_attrs** : attribute * [] (line 67)

## Macros (3)

- **sdio_config_attr**(field,format_string,args...) (line 32)
- **sdio_info_attr**(num) (line 49)
- **to_sdio_driver**(d) (line 29)
