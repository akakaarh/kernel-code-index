# drivers/i2c/i2c-core-of-prober.c

Subsystem: drivers/i2c

## Functions (14)

### i2c_of_probe_component
- Return type: int
- Signature: i2c_of_probe_component(struct device * dev,const struct i2c_of_probe_cfg * cfg,void * ctx)
- Line: 127

### i2c_of_probe_enable_node
- Return type: static int
- Signature: i2c_of_probe_enable_node(struct device * dev,struct device_node * node)
- Line: 60

### i2c_of_probe_get_i2c_node
- Return type: static device_node *
- Signature: i2c_of_probe_get_i2c_node(struct device * dev,const char * type)
- Line: 38

### i2c_of_probe_simple_cleanup
- Return type: void
- Signature: i2c_of_probe_simple_cleanup(struct device * dev,void * data)
- Line: 397

### i2c_of_probe_simple_cleanup_early
- Return type: void
- Signature: i2c_of_probe_simple_cleanup_early(struct device * dev,void * data)
- Line: 380

### i2c_of_probe_simple_disable_gpio
- Return type: static void
- Signature: i2c_of_probe_simple_disable_gpio(struct device * dev,struct i2c_of_probe_simple_ctx * ctx)
- Line: 300

### i2c_of_probe_simple_disable_regulator
- Return type: static void
- Signature: i2c_of_probe_simple_disable_regulator(struct device * dev,struct i2c_of_probe_simple_ctx * ctx)
- Line: 239

### i2c_of_probe_simple_enable
- Return type: int
- Signature: i2c_of_probe_simple_enable(struct device * dev,struct device_node * bus_node,void * data)
- Line: 320

### i2c_of_probe_simple_enable_regulator
- Return type: static int
- Signature: i2c_of_probe_simple_enable_regulator(struct device * dev,struct i2c_of_probe_simple_ctx * ctx)
- Line: 220

### i2c_of_probe_simple_get_gpiod
- Return type: static int
- Signature: i2c_of_probe_simple_get_gpiod(struct device * dev,struct device_node * node,struct i2c_of_probe_simple_ctx * ctx)
- Line: 249

### i2c_of_probe_simple_get_supply
- Return type: static int
- Signature: i2c_of_probe_simple_get_supply(struct device * dev,struct device_node * node,struct i2c_of_probe_simple_ctx * ctx)
- Line: 186

### i2c_of_probe_simple_put_gpiod
- Return type: static void
- Signature: i2c_of_probe_simple_put_gpiod(struct i2c_of_probe_simple_ctx * ctx)
- Line: 275

### i2c_of_probe_simple_put_supply
- Return type: static void
- Signature: i2c_of_probe_simple_put_supply(struct i2c_of_probe_simple_ctx * ctx)
- Line: 214

### i2c_of_probe_simple_set_gpio
- Return type: static int
- Signature: i2c_of_probe_simple_set_gpio(struct device * dev,struct i2c_of_probe_simple_ctx * ctx)
- Line: 281

## Variables (2)

- static **i2c_of_probe_dummy_ops** : const struct i2c_of_probe_ops (line 90)
- **i2c_of_probe_simple_ops** : i2c_of_probe_ops (line 410)
