import torch
from torch import tensor


class ImageColorLogic:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("BOOLEAN", "INT")
    CATEGORY = "Roy"
    FUNCTION = "execute"

    def execute(self, image: tensor):
        values = []
        for i in image:
            # h, w, c = i.shape
            unique_values, counts = torch.unique(i[0].view(i[0].shape[0], -1), return_counts=True, dim=1)
            if unique_values.shape[1] == 1:
                values.append(
                    (True, int(i[0][0][0].item()))
                )
            else:
                return False, -1
        color = values[0][1]
        for i in values:
            if i[1] != color:
                return True, -1
        return True, color


NODE_CLASS_MAPPINGS = {
    "ImageColorLogic🍺": ImageColorLogic,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageColorLogic🍺": "ImageColorLogic",
}
