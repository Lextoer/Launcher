cmake_minimum_required(VERSION 3.5)
project(shapes)

# Gerekli bağımlılıkları ekle
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Python paketini kur
ament_python_install_package(${PROJECT_NAME})

# Mesaj ve servis dosyalarını işaretle (eğer varsa)
# rosidl_generate_interfaces(${PROJECT_NAME}
#   "srv/Triangle.srv"
#   "msg/Dimensions.msg"
# )

# Yürütülebilir dosyaları yükle (örneğin shapes.py)
install(
  PROGRAMS
  shapes/shapes.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
