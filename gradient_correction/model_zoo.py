from tensorflow import keras


def cnn_deep(input_shape, output_shape, activation='relu', num_filters=24, first_layer_kernel_size=19, initializer='he_normal'):
    l2 = keras.regularizers.l2(1e-6) 

    # input layer
    inputs = keras.layers.Input(shape=input_shape)

    # layer 1 
    nn = keras.layers.Conv1D(filters=num_filters, kernel_size=first_layer_kernel_size, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(inputs)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation(activation)(nn)
    nn = keras.layers.Dropout(0.1)(nn)

    # layer 2
    nn = keras.layers.Conv1D(filters=32, kernel_size=7, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.2)(nn)
    nn = keras.layers.MaxPool1D(pool_size=4)(nn)

    # layer 3
    nn = keras.layers.Conv1D(filters=48, kernel_size=7, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.3)(nn)
    nn = keras.layers.MaxPool1D(pool_size=4)(nn)

    # layer 4
    nn = keras.layers.Conv1D(filters=64, kernel_size=3, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.4)(nn)
    nn = keras.layers.MaxPool1D(pool_size=3)(nn)

    # layer 5
    nn = keras.layers.Flatten()(nn)
    nn = keras.layers.Dense(96, kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.5)(nn)

    # Output layer 
    logits = keras.layers.Dense(output_shape, activation='linear')(nn)
    outputs = keras.layers.Activation('sigmoid')(logits)
        
    return keras.Model(inputs=inputs, outputs=outputs)




def cnn_shallow(input_shape, output_shape, activation='relu', num_filters=24, first_layer_kernel_size=19, initializer='he_normal'):
   
    l2 = keras.regularizers.l2(1e-6) 
    
    # input layer
    inputs = keras.layers.Input(shape=input_shape)

    # layer 1 
    nn = keras.layers.Conv1D(filters=num_filters, kernel_size=first_layer_kernel_size, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(inputs)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation(activation)(nn)
    nn = keras.layers.Dropout(0.1)(nn)
    nn = keras.layers.MaxPool1D(pool_size=50)(nn)

    # layer 2
    nn = keras.layers.Conv1D(filters=48, kernel_size=3, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.2)(nn)
    nn = keras.layers.MaxPool1D(pool_size=2)(nn)

    # layer 3
    nn = keras.layers.Flatten()(nn)
    nn = keras.layers.Dense(96, kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.5)(nn)

    # Output layer 
    logits = keras.layers.Dense(output_shape, activation='linear')(nn)
    outputs = keras.layers.Activation('sigmoid')(logits)
        
    return keras.Model(inputs=inputs, outputs=outputs)

  
def cnn_deep_init(input_shape, output_shape, activation='relu', num_filters=24, first_layer_kernel_size=19, sigma=0.05):
    l2 = keras.regularizers.l2(1e-6)     
    initializer = keras.initializers.RandomNormal(mean=0.0, stddev=sigma)

    # input layer
    inputs = keras.layers.Input(shape=input_shape)

    # layer 1 
    nn = keras.layers.Conv1D(filters=num_filters, kernel_size=first_layer_kernel_size, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(inputs)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation(activation)(nn)
    nn = keras.layers.Dropout(0.1)(nn)

    # layer 2
    nn = keras.layers.Conv1D(filters=32, kernel_size=7, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.2)(nn)
    nn = keras.layers.MaxPool1D(pool_size=4)(nn)

    # layer 3
    nn = keras.layers.Conv1D(filters=48, kernel_size=7, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.3)(nn)
    nn = keras.layers.MaxPool1D(pool_size=4)(nn)

    # layer 4
    nn = keras.layers.Conv1D(filters=64, kernel_size=3, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.4)(nn)
    nn = keras.layers.MaxPool1D(pool_size=3)(nn)

    # layer 5
    nn = keras.layers.Flatten()(nn)
    nn = keras.layers.Dense(96, kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.5)(nn)

    # Output layer 
    logits = keras.layers.Dense(output_shape, activation='linear')(nn)
    outputs = keras.layers.Activation('sigmoid')(logits)
        
    return keras.Model(inputs=inputs, outputs=outputs)




def cnn_shallow_init(input_shape, output_shape, activation='relu', num_filters=24, first_layer_kernel_size=19, sigma=0.05):
    l2 = keras.regularizers.l2(1e-6)   
    initializer = keras.initializers.RandomNormal(mean=0.0, stddev=sigma)
    
    # input layer
    inputs = keras.layers.Input(shape=input_shape)

    # layer 1 
    nn = keras.layers.Conv1D(filters=num_filters, kernel_size=first_layer_kernel_size, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(inputs)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation(activation)(nn)
    nn = keras.layers.Dropout(0.1)(nn)
    nn = keras.layers.MaxPool1D(pool_size=50)(nn)

    # layer 2
    nn = keras.layers.Conv1D(filters=48, kernel_size=3, padding='same', 
                             kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.2)(nn)
    nn = keras.layers.MaxPool1D(pool_size=2)(nn)

    # layer 3
    nn = keras.layers.Flatten()(nn)
    nn = keras.layers.Dense(96, kernel_regularizer=l2, kernel_initializer=initializer)(nn)     
    nn = keras.layers.BatchNormalization()(nn)
    nn = keras.layers.Activation('relu')(nn)
    nn = keras.layers.Dropout(0.5)(nn)

    # Output layer 
    logits = keras.layers.Dense(output_shape, activation='linear')(nn)
    outputs = keras.layers.Activation('sigmoid')(logits)
        
    return keras.Model(inputs=inputs, outputs=outputs)
