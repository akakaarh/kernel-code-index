# drivers/mmc/core/pwrseq_sd8787.c

Subsystem: drivers/mmc

## Functions (6)

### mmc_pwrseq_sd8787_power_off
- Return type: static void
- Signature: mmc_pwrseq_sd8787_power_off(struct mmc_host * host)
- Line: 45

### mmc_pwrseq_sd8787_pre_power_on
- Return type: static void
- Signature: mmc_pwrseq_sd8787_pre_power_on(struct mmc_host * host)
- Line: 35

### mmc_pwrseq_sd8787_probe
- Return type: static int
- Signature: mmc_pwrseq_sd8787_probe(struct platform_device * pdev)
- Line: 88

### mmc_pwrseq_sd8787_remove
- Return type: static void
- Signature: mmc_pwrseq_sd8787_remove(struct platform_device * pdev)
- Line: 116

### mmc_pwrseq_wilc1000_power_off
- Return type: static void
- Signature: mmc_pwrseq_wilc1000_power_off(struct mmc_host * host)
- Line: 63

### mmc_pwrseq_wilc1000_pre_power_on
- Return type: static void
- Signature: mmc_pwrseq_wilc1000_pre_power_on(struct mmc_host * host)
- Line: 53

## Structs (1)

### mmc_pwrseq_sd8787
- Line: 27
- Members:
  - pwrseq: mmc_pwrseq
  - reset_gpio: gpio_desc *
  - pwrdn_gpio: gpio_desc *

## Variables (4)

- static **mmc_pwrseq_sd8787_driver** : platform_driver (line 123)
- static **mmc_pwrseq_sd8787_of_match** : const struct of_device_id[] (line 81)
- static **mmc_pwrseq_sd8787_ops** : const struct mmc_pwrseq_ops (line 71)
- static **mmc_pwrseq_wilc1000_ops** : const struct mmc_pwrseq_ops (line 76)

## Macros (1)

- **to_pwrseq_sd8787**(p) (line 33)
