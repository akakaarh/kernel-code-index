# drivers/spi/spi-offload-trigger-adi-util-sigma-delta.c

Subsystem: drivers/spi

## Functions (2)

### adi_util_sigma_delta_match
- Return type: static bool
- Signature: adi_util_sigma_delta_match(struct spi_offload_trigger * trigger,enum spi_offload_trigger_type type,u64 * args,u32 nargs)
- Line: 18

### adi_util_sigma_delta_probe
- Return type: static int
- Signature: adi_util_sigma_delta_probe(struct platform_device * pdev)
- Line: 29

## Variables (3)

- static **adi_util_sigma_delta_driver** : platform_driver (line 51)
- static **adi_util_sigma_delta_of_match_table** : const struct of_device_id[] (line 45)
- static **adi_util_sigma_delta_ops** : const struct spi_offload_trigger_ops (line 25)
