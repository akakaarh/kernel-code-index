# drivers/i2c/busses/i2c-amd-mp2-pci.c

Subsystem: drivers/i2c

## Functions (20)

### __amd_mp2_process_event
- Return type: static void
- Signature: __amd_mp2_process_event(struct amd_i2c_common * i2c_common)
- Line: 134

### amd_mp2_bus_enable_set
- Return type: int
- Signature: amd_mp2_bus_enable_set(struct amd_i2c_common * i2c_common,bool enable)
- Line: 57

### amd_mp2_c2p_mutex_lock
- Return type: static void
- Signature: amd_mp2_c2p_mutex_lock(struct amd_i2c_common * i2c_common)
- Line: 19

### amd_mp2_c2p_mutex_unlock
- Return type: static void
- Signature: amd_mp2_c2p_mutex_unlock(struct amd_i2c_common * i2c_common)
- Line: 28

### amd_mp2_clear_reg
- Return type: static void
- Signature: amd_mp2_clear_reg(struct amd_mp2_dev * privdata)
- Line: 277

### amd_mp2_cmd
- Return type: static int
- Signature: amd_mp2_cmd(struct amd_i2c_common * i2c_common,union i2c_cmd_base i2c_cmd_base)
- Line: 42

### amd_mp2_cmd_rw_fill
- Return type: static void
- Signature: amd_mp2_cmd_rw_fill(struct amd_i2c_common * i2c_common,union i2c_cmd_base * i2c_cmd_base,enum i2c_cmd reqcmd)
- Line: 75

### amd_mp2_find_device
- Return type: amd_mp2_dev *
- Signature: amd_mp2_find_device(void)
- Line: 457

### amd_mp2_irq_isr
- Return type: static irqreturn_t
- Signature: amd_mp2_irq_isr(int irq,void * dev)
- Line: 201

### amd_mp2_pci_check_rw_event
- Return type: static void
- Signature: amd_mp2_pci_check_rw_event(struct amd_i2c_common * i2c_common)
- Line: 110

### amd_mp2_pci_init
- Return type: static int
- Signature: amd_mp2_pci_init(struct amd_mp2_dev * privdata,struct pci_dev * pci_dev)
- Line: 288

### amd_mp2_pci_probe
- Return type: static int
- Signature: amd_mp2_pci_probe(struct pci_dev * pci_dev,const struct pci_device_id * id)
- Line: 342

### amd_mp2_pci_remove
- Return type: static void
- Signature: amd_mp2_pci_remove(struct pci_dev * pci_dev)
- Line: 370

### amd_mp2_pci_resume
- Return type: static int
- Signature: amd_mp2_pci_resume(struct device * dev)
- Line: 407

### amd_mp2_pci_suspend
- Return type: static int
- Signature: amd_mp2_pci_suspend(struct device * dev)
- Line: 383

### amd_mp2_process_event
- Return type: void
- Signature: amd_mp2_process_event(struct amd_i2c_common * i2c_common)
- Line: 183

### amd_mp2_register_cb
- Return type: int
- Signature: amd_mp2_register_cb(struct amd_i2c_common * i2c_common)
- Line: 248

### amd_mp2_rw
- Return type: int
- Signature: amd_mp2_rw(struct amd_i2c_common * i2c_common,enum i2c_cmd reqcmd)
- Line: 86

### amd_mp2_rw_timeout
- Return type: void
- Signature: amd_mp2_rw_timeout(struct amd_i2c_common * i2c_common)
- Line: 241

### amd_mp2_unregister_cb
- Return type: int
- Signature: amd_mp2_unregister_cb(struct amd_i2c_common * i2c_common)
- Line: 267

## Variables (2)

- static **amd_mp2_pci_driver** : pci_driver (line 444)
- static **amd_mp2_pci_tbl** : const struct pci_device_id[] (line 438)
