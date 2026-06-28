# CSharp el using
Este al usarse en objetos tipo connection, o reader, se cierran solos.
Por ejemplo `using SqLiteConnection connection = Connect()`. Al abrir, cierra en automatico. Si no se usa el using, tienes que psarle un `conneciton.Close()`.
