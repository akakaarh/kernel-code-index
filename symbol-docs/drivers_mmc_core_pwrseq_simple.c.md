# drivers/mmc/core/pwrseq_simple.c

Subsystem: drivers/mmc

## Functions (6)

### mmc_pwrseq_simple_post_power_on
- Return type: static void
- Signature: mmc_pwrseq_simple_post_power_on(struct mmc_host * host)
- Line: 79

### mmc_pwrseq_simple_power_off
- Return type: static void
- Signature: mmc_pwrseq_simple_power_off(struct mmc_host * host)
- Line: 92

### mmc_pwrseq_simple_pre_power_on
- Return type: static void
- Signature: mmc_pwrseq_simple_pre_power_on(struct mmc_host * host)
- Line: 63

### mmc_pwrseq_simple_probe
- Return type: static int
- Signature: mmc_pwrseq_simple_probe(struct platform_device * pdev)
- Line: 123

### mmc_pwrseq_simple_remove
- Return type: static void
- Signature: mmc_pwrseq_simple_remove(struct platform_device * pdev)
- Line: 172

### mmc_pwrseq_simple_set_gpios_value
- Return type: static void
- Signature: mmc_pwrseq_simple_set_gpios_value(struct mmc_pwrseq_simple * pwrseq,int value)
- Line: 39

## Structs (1)

### mmc_pwrseq_simple
- Line: 27
- Members:
  - pwrseq: mmc_pwrseq
  - clk_enabled: bool
  - post_power_on_delay_ms: u32
  - power_off_delay_us: u32
  - ext_clk: clk *
  - reset_gpios: gpio_descs *
  - reset_ctrl: reset_control *

## Variables (3)

- static **mmc_pwrseq_simple_driver** : platform_driver (line 179)
- static **mmc_pwrseq_simple_of_match** : const struct of_device_id[] (line 117)
- static **mmc_pwrseq_simple_ops** : const struct mmc_pwrseq_ops (line 111)

## Macros (1)

- **to_pwrseq_simple**(p) (line 37)
