# drivers/spi/spi-offload-trigger-pwm.c

Subsystem: drivers/spi

## Functions (6)

### spi_offload_trigger_pwm_disable
- Return type: static void
- Signature: spi_offload_trigger_pwm_disable(struct spi_offload_trigger * trigger)
- Line: 87

### spi_offload_trigger_pwm_enable
- Return type: static int
- Signature: spi_offload_trigger_pwm_enable(struct spi_offload_trigger * trigger,struct spi_offload_trigger_config * config)
- Line: 66

### spi_offload_trigger_pwm_match
- Return type: static bool
- Signature: spi_offload_trigger_pwm_match(struct spi_offload_trigger * trigger,enum spi_offload_trigger_type type,u64 * args,u32 nargs)
- Line: 27

### spi_offload_trigger_pwm_probe
- Return type: static int
- Signature: spi_offload_trigger_pwm_probe(struct platform_device * pdev)
- Line: 118

### spi_offload_trigger_pwm_release
- Return type: static void
- Signature: spi_offload_trigger_pwm_release(void * data)
- Line: 113

### spi_offload_trigger_pwm_validate
- Return type: static int
- Signature: spi_offload_trigger_pwm_validate(struct spi_offload_trigger * trigger,struct spi_offload_trigger_config * config)
- Line: 37

## Structs (1)

### spi_offload_trigger_pwm_state
- Line: 22
- Members:
  - dev: device *
  - pwm: pwm_device *

## Variables (3)

- static **spi_offload_trigger_pwm_driver** : platform_driver (line 161)
- static **spi_offload_trigger_pwm_of_match_table** : const struct of_device_id[] (line 155)
- static **spi_offload_trigger_pwm_ops** : const struct spi_offload_trigger_ops (line 106)
