"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from google.generativeai.types import HarmCategory, HarmBlockThreshold



# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
def gemini_api(source_text,key):
  os.environ["GEMINI_API_KEY"] = key

  genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 4096,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings={
          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
      }
  )
  chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "dịch bài bào này sang tiếng anh, không cần xuống hàng:\n\"Thời tiết Hà Nội 3 ngày tới: Mưa giông mạnh, nguy cơ lốc sét và ngập úng\nDự báo thời tiết Hà Nội 3 ngày tới (29-31/7), mưa lớn dồn dập, nguy cơ có gió giật mạnh, lốc sét và ngập úng ở những vùng trũng.\nTheo chuyên gia Trung tâm dự báo khí tượng thủy văn quốc gia, thời tiết Hà Nội ngày 29-30/7, nhiều mây, có mưa vừa đến mưa to, có nơi mưa rất to và giông, trong mưa giông có khả năng xảy ra lốc, sét và gió giật mạnh.\nSang ngày 31/7, khu vực giảm mưa, còn ở mức mưa rào và giông.\nNhiệt độ cao nhất trong 2 ngày đầu khoảng 32 độ, sau đó tăng lên 34 độ; nhiệt độ ban đêm 25-27 độ.\nĐài khí tượng thủy văn khu vực đồng bằng và trung du Bắc Bộ cũng dự báo, ngày 30/7, lượng mưa ở Hà Nội từ 50-100mm, có nơi cao hơn 120mm; từ đêm 30 đến ngày 31/7, giảm còn ở mức 10-20mm.\nCơ quan khí tượng cảnh báo, lũ trên các sông Tích, sông Bùi đang ở mức cao nên khả năng tiếp tục gây rủi ro thiên tai, thiệt hại về người và tài sản, nhất là vùng ven sông các huyện: Chương Mỹ, Mỹ Đức, Quốc Oai, Thạch Thất...\nNgoài ra, Trung tâm dự báo khí tượng thủy văn quốc gia cho biết, do ảnh hưởng của rãnh áp thấp có trục qua Bắc Bộ kết hợp hội tụ gió trên cao nên từ sáng 29 đến sáng 31/7, ở Bắc Bộ có mưa vừa, mưa to và giông, cục bộ có nơi mưa rất to với tổng lượng mưa phổ biến ở khu vực vùng núi và trung du Bắc Bộ là 50-120mm, cục bộ có nơi trên 250mm; đồng bằng Bắc Bộ 30-100mm, cục bộ có nơi trên 150mm.\nCảnh báo ngày 31/7, ở khu vực này tiếp tục có mưa vừa, mưa to và giông, cục bộ có nơi mưa rất to. Từ đêm 31/7, mưa lớn ở Bắc Bộ có khả năng giảm dần.\nDưới tác động của mưa lớn, cơ quan khí tượng lưu ý, cần đề phòng nguy cơ xảy ra lũ quét, sạt lở đất tại khu vực vùng núi và ngập úng tại các khu vực trũng, thấp. Đề phòng mưa với cường độ lớn trong một thời gian ngắn gây ngập úng tại các khu đô thị. Trong mưa giông có khả năng xảy ra lốc, sét và gió giật mạnh.\nThời tiết tại thủ đô Hà Nội trong 3 ngày tới (29-31/7):\nNhiều mây, có mưa vừa đến mưa to và giông, trong mưa giông đề phòng lốc, sét, gió giật mạnh.Nhiệt độ cao nhất: 30-32 độĐộ ẩm trung bình: 70-75%Khả năng mưa: 80-85%\nNhiều mây, có mưa vừa đến mưa to và giông, trong mưa giông đề phòng lốc, sét, gió giật mạnh. Nhiệt độ thấp nhất: 25-27 độĐộ ẩm trung bình: 88-98%Khả năng mưa: 80-85%\nNhiều mây, có mưa vừa và giông, trong mưa giông đề phòng lốc, sét, gió giật mạnh.Nhiệt độ cao nhất: 30-32 độĐộ ẩm trung bình: 70-75%Khả năng mưa: 80-85%\nNhiều mây, có mưa rào và giông.Nhiệt độ thấp nhất: 25-27 độĐộ ẩm trung bình: 88-98%Khả năng mưa: 80-85%\nNhiều mây, có lúc có mưa rào.Nhiệt độ cao nhất: 32-34 độĐộ ẩm trung bình: 70-75%Khả năng mưa: 70-75%\nNhiều mây, không mưa.Nhiệt độ thấp nhất: 25-27 độĐộ ẩm trung bình: 85-95%Khả năng mưa: 30-40%\n\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hanoi weather forecast for the next 3 days: Heavy thunderstorms, risk of tornadoes and flooding The weather forecast for Hanoi for the next 3 days (July 29-31) predicts heavy rain, with risks of strong gusts, tornadoes and flooding in low-lying areas. According to experts from the National Center for Hydro-meteorological Forecasting, the weather in Hanoi on July 29-30 will be cloudy, with moderate to heavy rain, and some areas experiencing very heavy rain and thunderstorms. Thunderstorms may bring tornadoes, lightning, and strong winds. On July 31, the rain will subside, with only scattered showers and thunderstorms. The highest temperature in the first 2 days will be around 32 degrees, then rising to 34 degrees; the lowest temperature at night will be 25-27 degrees. The Regional Hydro-meteorological Station for the Northern Plains and Midlands also forecasts that on July 30, the rainfall in Hanoi will be 50-100mm, and in some places higher than 120mm; from the night of July 30 to July 31, it will decrease to 10-20mm. The meteorological agency warns that the floods on the Tich and Bui rivers are at high levels, so there is a risk of continued natural disasters and damage to people and property, especially in the riverside areas of the districts of Chuong My, My Duc, Quoc Oai, and Thach That. In addition, the National Center for Hydro-meteorological Forecasting said that due to the influence of a low-pressure trough passing through the North Central region combined with high-altitude wind convergence, from the morning of July 29 to the morning of July 31, the North Central region will experience moderate to heavy rain and thunderstorms, with some areas experiencing very heavy rain with a total rainfall in the mountainous and midland areas of the North Central region of 50-120mm, and in some places over 250mm; the Northern Delta will have 30-100mm, and in some places over 150mm. The warning for July 31 is that this area will continue to have moderate to heavy rain and thunderstorms, with some areas experiencing very heavy rain. From the night of July 31, the heavy rain in the North Central region is likely to gradually decrease. Due to the impact of heavy rain, the meteorological agency advises that it is necessary to be on guard against the risk of flash floods, landslides in mountainous areas, and flooding in low-lying areas. Be on guard against heavy rainfall in a short period of time causing flooding in urban areas. Thunderstorms may bring tornadoes, lightning, and strong winds. Weather forecast for Hanoi in the next 3 days (July 29-31): Cloudy, with moderate to heavy rain and thunderstorms, during thunderstorms beware of tornadoes, lightning, and strong gusts. Highest temperature: 30-32 degrees Average humidity: 70-75% Chance of rain: 80-85% Cloudy, with moderate to heavy rain and thunderstorms, during thunderstorms beware of tornadoes, lightning, and strong gusts. Lowest temperature: 25-27 degrees Average humidity: 88-98% Chance of rain: 80-85% Cloudy, with moderate rain and thunderstorms, during thunderstorms beware of tornadoes, lightning, and strong gusts. Highest temperature: 30-32 degrees Average humidity: 70-75% Chance of rain: 80-85% Cloudy, with scattered showers and thunderstorms. Lowest temperature: 25-27 degrees Average humidity: 88-98% Chance of rain: 80-85% Cloudy, occasional showers. Highest temperature: 32-34 degrees Average humidity: 70-75% Chance of rain: 70-75% Cloudy, no rain. Lowest temperature: 25-27 degrees Average humidity: 85-95% Chance of rain: 30-40%",
      ],
    },
    {
      "role": "user",
      "parts": [
        "dịch bài bào này sang tiếng anh, không cần xuống hàng:\n\"Luật Trật tự, an toàn giao thông đường bộ: Lúc nào không được bấm còi?\nKhông được bấm còi từ 22h hôm trước đến 5h hôm sau hoặc bấm còi liên tục trong khu đông dân cư, cơ sở khám chữa bệnh.\nLuật sư Nguyễn Văn Điện (Đoàn Luật sư TP Hà Nội) cho biết, Điều 21, Luật Trật tự, an toàn giao thông đường bộ vừa được Quốc hội thông qua và có hiệu lực từ 1/1/2025 quy định rõ về sử dụng tín hiệu còi. Đây là nội dung cũng đã được quy định tại  Điều 8, Luật Giao thông đường bộ năm 2008. \nTheo đó, người điều khiển phương tiện giao thông chỉ được dùng còi trong các trường hợp: Báo hiệu cho người tham gia giao thông đường bộ khi xuất hiện tình huống có thể mất an toàn giao thông; Báo hiệu chuẩn bị vượt xe.\nNgoài ra, luật cũng quy định không được sử dụng còi liên tục, không sử dụng còi có âm lượng không đúng quy định, không dùng còi trong thời gian từ 22h ngày hôm trước đến 5h ngày hôm sau trong khu đông dân cư, khu vực cơ sở khám bệnh, chữa bệnh (trừ xe ưu tiên).\nNhư vậy, người tham gia giao thông bằng ô tô, xe máy và các loại xe tương tự không được bấm còi liên tục ở bất cứ nơi đâu và bất cứ giờ nào.\nĐặc biệt, không được sử dụng còi xe trong khoảng thời gian từ 22h - 5h hoặc sử dụng còi hơi vào bất cứ giờ nào khi đi trong khi đô thị, khu đông dân cư.\n“Việc bấm còi không \"đúng nơi đúng chỗ\" có thể bị phạt nặng theo quy định tại Nghị định 100/2019/NĐ-CP (Nghị định 100) về xử phạt hành chính trong lĩnh vực giao thông đường bộ, đường sắt.\nCụ thể, Điều 5, Nghị định 100 phạt tiền từ 300.000 - 400.000 đồng nếu bấm còi trong đô thị và khu đông dân cư trong thời gian từ 22h ngày hôm trước đến 5h ngày hôm sau; bấm còi tại nơi có biển báo cấm sử dụng còi trừ các xe ưu tiên theo quy định.\nNgoài ra, người điều khiển phương tiện bị phạt tiền từ 800.000 - 1.000.000 đồng nếu bấm còi liên tục; bấm còi hơi trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định”, luật sư Điện phân tích.\nĐối với mô tô, xe máy, việc sử dụng còi sai quy định cũng bị xử phạt. Cụ thể, tại Điều 6, Nghị định 100 quy định phạt tiền từ 100.000 - 200.000 đồng đối với người điều khiển nếu bấm còi từ từ 22h ngày hôm trước đến 5h ngày hôm sau trong khu đô thị, khu đông dân cư; bấm còi ở nơi cấm sử dụng còi.\nNếu bấm còi liên tục trong đô thị, khu đông dân cư, người điều khiển mô tô, xe máy bị phạt tiền từ 400.000 – 600.000 đồng.\nPhải tắt đèn chiếu xa trong tình huống nào?\nĐiều 20, Luật Trật tự, an toàn giao thông đường bộ quy định về việc sử dụng đèn của phương tiện khi tham gia giao thông.\nTheo đó, luật nêu rõ, người lái xe, người điều khiển xe máy chuyên dùng tham gia giao thông đường bộ phải bật đèn chiếu sáng phía trước trong thời gian từ 18h ngày hôm trước đến 6h ngày hôm sau hoặc khi có sương mù, khói, bụi, trời mưa, thời tiết xấu làm hạn chế tầm nhìn.\nNgười lái xe, người điều khiển xe máy chuyên dùng phải tắt đèn chiếu xa, bật đèn chiếu gần trong các trường hợp sau đây:\nKhi gặp người đi bộ qua đường.\nKhi đi trên các đoạn đường qua khu đông dân cư có hệ thống chiếu sáng đang hoạt động.\nKhi gặp xe đi ngược chiều, trừ trường hợp dải phân cách có khả năng chống chói.\nKhi chuyển hướng xe tại nơi đường giao nhau.\n\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Road Traffic Safety Law: When is it not allowed to honk the horn? Do not honk the horn from 10 p.m. the previous day to 5 a.m. the following day or honk the horn continuously in heavily populated areas or at medical facilities. Lawyer Nguyen Van Dien (Hanoi Bar Association) said that Article 21 of the Law on Road Traffic Safety, which was recently passed by the National Assembly and will take effect from January 1, 2025, clearly regulates the use of horn signals. This content has also been regulated in Article 8 of the 2008 Law on Road Traffic. Accordingly, drivers are only allowed to use horns in the following cases: Signaling to other road users when there is a situation that may result in the loss of traffic safety Signaling to prepare to overtake. In addition, the law also stipulates that it is not allowed to use horns continuously, not to use horns with non-standard volume, and not to use horns from 10 p.m. the previous day to 5 a.m. the following day in densely populated areas, areas of medical examination and treatment facilities (except priority vehicles). Thus, participants in traffic by car, motorbike, and similar vehicles are not allowed to honk the horn continuously anywhere and at any time. In particular, car horns must not be used between the hours of 10 p.m. and 5 a.m. or air horns must not be used at any time when driving in urban areas or densely populated areas. \"The act of honking the horn in the \"wrong place at the wrong time\" can be severely punished according to the provisions of Decree 100/2019/ND-CP (Decree 100) on administrative sanctions in the field of road and rail traffic. Specifically, Article 5 of Decree 100 imposes a fine of from 300,000 to 400,000 VND for honking horns in urban areas and densely populated areas between 10 p.m. the previous day and 5 a.m. the following day; honking the horn where there is a sign prohibiting the use of horns, except for priority vehicles as prescribed. In addition, drivers will be fined from 800,000 to 1,000,000 VND for honking the horn continuously; honking the horn in urban areas or densely populated areas, except for priority vehicles performing duties as prescribed,\" analyzed lawyer Dien. For motorbikes, using the horn in violation of regulations is also subject to fines. Specifically, Article 6 of Decree 100 stipulates a fine of from 100,000 to 200,000 VND for drivers who honk the horn from 10 p.m. the previous day to 5 a.m. the following day in urban areas or densely populated areas; honking the horn in places where it is prohibited to use the horn. If they honk the horn continuously in urban areas or densely populated areas, drivers of motorbikes will be fined from 400,000 to 600,000 VND. When is it necessary to turn off the high beam? Article 20 of the Law on Road Traffic Safety regulates the use of vehicle lights when participating in traffic. Accordingly, the law clearly states that drivers and drivers of specialized motorbikes participating in road traffic must turn on the headlights from 6 p.m. the previous day to 6 a.m. the following day or when there is fog, smoke, dust, rain, bad weather that limits visibility. Drivers and drivers of specialized motorbikes must turn off the high beam and turn on the low beam in the following cases: When pedestrians are crossing the road. When driving on roads through densely populated areas where the lighting system is in operation. When meeting vehicles traveling in the opposite direction, except when the median strip has glare protection. When changing direction of the vehicle at the intersection.",
      ],
    },
  ]
)
  temp = chat_session.send_message("dịch bài bào này sang tiếng anh, không cần xuống hàng:\n\ " + source_text)
  return temp.text
 