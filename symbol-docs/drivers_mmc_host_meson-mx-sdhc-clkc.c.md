# drivers/mmc/host/meson-mx-sdhc-clkc.c

Subsystem: drivers/mmc

## Functions (3)

### meson_mx_sdhc_clk_hw_register
- Return type: static int
- Signature: meson_mx_sdhc_clk_hw_register(struct device * dev,const char * name_suffix,const struct clk_parent_data * parents,unsigned int num_parents,const struct clk_ops * ops,struct clk_hw * hw)
- Line: 47

### meson_mx_sdhc_gate_clk_hw_register
- Return type: static int
- Signature: meson_mx_sdhc_gate_clk_hw_register(struct device * dev,const char * name_suffix,struct clk_hw * parent,struct clk_hw * hw,struct clk_bulk_data * clk_bulk_data,u8 bulk_index)
- Line: 71

### meson_mx_sdhc_register_clkc
- Return type: int
- Signature: meson_mx_sdhc_register_clkc(struct device * dev,void __iomem * base,struct clk_bulk_data * clk_bulk_data)
- Line: 91

## Structs (1)

### meson_mx_sdhc_clkc
- Line: 15
- Members:
  - src_sel: clk_mux
  - div: clk_divider
  - mod_clk_en: clk_gate
  - tx_clk_en: clk_gate
  - rx_clk_en: clk_gate
  - sd_clk_en: clk_gate

## Variables (2)

- static **meson_mx_sdhc_div_table** : const struct clk_div_table[] (line 31)
- static **meson_mx_sdhc_src_sel_parents** : const struct clk_parent_data[4] (line 24)
