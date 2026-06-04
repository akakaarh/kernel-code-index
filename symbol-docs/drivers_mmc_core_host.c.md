# drivers/mmc/core/host.c

Subsystem: drivers/mmc

## Functions (27)

### devm_mmc_alloc_host
- Return type: mmc_host *
- Signature: devm_mmc_alloc_host(struct device * dev,int extra)
- Line: 589

### devm_mmc_host_release
- Return type: static void
- Signature: devm_mmc_host_release(struct device * dev,void * res)
- Line: 584

### mmc_add_host
- Return type: int
- Signature: mmc_add_host(struct mmc_host * host)
- Line: 649

### mmc_alloc_host
- Return type: mmc_host *
- Signature: mmc_alloc_host(int extra,struct device * dev)
- Line: 512

### mmc_first_nonreserved_index
- Return type: static int
- Signature: mmc_first_nonreserved_index(void)
- Line: 494

### mmc_free_host
- Return type: void
- Signature: mmc_free_host(struct mmc_host * host)
- Line: 698

### mmc_host_class_complete
- Return type: static void
- Signature: mmc_host_class_complete(struct device * dev)
- Line: 54

### mmc_host_class_prepare
- Return type: static int
- Signature: mmc_host_class_prepare(struct device * dev)
- Line: 36

### mmc_host_classdev_release
- Return type: static void
- Signature: mmc_host_classdev_release(struct device * dev)
- Line: 66

### mmc_host_classdev_shutdown
- Return type: static int
- Signature: mmc_host_classdev_shutdown(struct device * dev)
- Line: 75

### mmc_of_parse
- Return type: int
- Signature: mmc_of_parse(struct mmc_host * host)
- Line: 265

### mmc_of_parse_clk_phase
- Return type: void
- Signature: mmc_of_parse_clk_phase(struct device * dev,struct mmc_clk_phase_map * map)
- Line: 229

### mmc_of_parse_timing_phase
- Return type: static void
- Signature: mmc_of_parse_timing_phase(struct device * dev,const char * prop,struct mmc_clk_phase * phase)
- Line: 214

### mmc_of_parse_voltage
- Return type: int
- Signature: mmc_of_parse_voltage(struct mmc_host * host,u32 * mask)
- Line: 438

### mmc_register_host_class
- Return type: int
- Signature: mmc_register_host_class(void)
- Line: 90

### mmc_remove_host
- Return type: void
- Signature: mmc_remove_host(struct mmc_host * host)
- Line: 679

### mmc_retune
- Return type: int
- Signature: mmc_retune(struct mmc_host * host)
- Line: 170

### mmc_retune_disable
- Return type: void
- Signature: mmc_retune_disable(struct mmc_host * host)
- Line: 140

### mmc_retune_enable
- Return type: void
- Signature: mmc_retune_enable(struct mmc_host * host)
- Line: 104

### mmc_retune_hold
- Return type: void
- Signature: mmc_retune_hold(struct mmc_host * host)
- Line: 154

### mmc_retune_pause
- Return type: void
- Signature: mmc_retune_pause(struct mmc_host * host)
- Line: 116

### mmc_retune_release
- Return type: void
- Signature: mmc_retune_release(struct mmc_host * host)
- Line: 161

### mmc_retune_timer
- Return type: static void
- Signature: mmc_retune_timer(struct timer_list * t)
- Line: 207

### mmc_retune_timer_stop
- Return type: void
- Signature: mmc_retune_timer_stop(struct mmc_host * host)
- Line: 148

### mmc_retune_unpause
- Return type: void
- Signature: mmc_retune_unpause(struct mmc_host * host)
- Line: 125

### mmc_unregister_host_class
- Return type: void
- Signature: mmc_unregister_host_class(void)
- Line: 95

### mmc_validate_host_caps
- Return type: static int
- Signature: mmc_validate_host_caps(struct mmc_host * host)
- Line: 610

## Variables (2)

- static **mmc_host_class** : const struct class (line 83)
- static **mmc_host_class_dev_pm_ops** : const struct dev_pm_ops (line 61)

## Macros (1)

- **cls_dev_to_mmc_host**(d) (line 32)
