# drivers/i2c/muxes/i2c-demux-pinctrl.c

Subsystem: drivers/i2c

## Functions (10)

### available_masters_show
- Return type: static ssize_t
- Signature: available_masters_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 162

### current_master_show
- Return type: static ssize_t
- Signature: current_master_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 178

### current_master_store
- Return type: static ssize_t
- Signature: current_master_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 187

### i2c_demux_activate_master
- Return type: static int
- Signature: i2c_demux_activate_master(struct i2c_demux_pinctrl_priv * priv,u32 new_chan)
- Line: 54

### i2c_demux_change_master
- Return type: static int
- Signature: i2c_demux_change_master(struct i2c_demux_pinctrl_priv * priv,u32 new_chan)
- Line: 148

### i2c_demux_deactivate_master
- Return type: static int
- Signature: i2c_demux_deactivate_master(struct i2c_demux_pinctrl_priv * priv)
- Line: 130

### i2c_demux_functionality
- Return type: static u32
- Signature: i2c_demux_functionality(struct i2c_adapter * adap)
- Line: 46

### i2c_demux_master_xfer
- Return type: static int
- Signature: i2c_demux_master_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 38

### i2c_demux_pinctrl_probe
- Return type: static int
- Signature: i2c_demux_pinctrl_probe(struct platform_device * pdev)
- Line: 208

### i2c_demux_pinctrl_remove
- Return type: static void
- Signature: i2c_demux_pinctrl_remove(struct platform_device * pdev)
- Line: 291

## Structs (2)

### i2c_demux_pinctrl_chan
- Line: 22
- Members:
  - parent_np: device_node *
  - parent_adap: i2c_adapter *
  - chgset: of_changeset
  - cur_chan: int
  - num_chan: int
  - dev: device *
  - bus_name: const char *
  - cur_adap: i2c_adapter
  - algo: i2c_algorithm

### i2c_demux_pinctrl_priv
- Line: 28
- Members:
  - parent_np: device_node *
  - parent_adap: i2c_adapter *
  - chgset: of_changeset
  - cur_chan: int
  - num_chan: int
  - dev: device *
  - bus_name: const char *
  - cur_adap: i2c_adapter
  - algo: i2c_algorithm

## Variables (2)

- static **i2c_demux_pinctrl_driver** : platform_driver (line 313)
- static **i2c_demux_pinctrl_of_match** : const struct of_device_id[] (line 307)
