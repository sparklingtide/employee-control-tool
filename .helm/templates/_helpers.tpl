{{/*
Return the proper backend image tag
*/}}
{{- define "backend.imageTag" -}}
{{- if .Values.image }}
{{ .Values.image.tag }}
{{- else -}}
{{ .Values.global.backend.image.tag }}
{{- end -}}
{{- end -}}

{{/*
Return the proper backend image name
*/}}
{{- define "backend.image" -}}
{{- if .Values.image }}
{{ include "common.images.image" ( dict "imageRoot" .Values.image ) }}
{{- else -}}
{{ include "common.images.image" ( dict "imageRoot" .Values.global.backend.image ) }}
{{- end -}}
{{- end -}}

{{/*
Render backend pullSecrets
*/}}
{{- define "backend.renderPullSecrets" -}}
{{- if .Values.image }}
{{ include "common.images.renderPullSecrets" ( dict "images" ( list .Values.image ) "context" . )  }}
{{- else -}}
{{ include "common.images.renderPullSecrets" ( dict "images" ( list .Values.global.backend.image ) "context" . )  }}
{{- end -}}
{{- end -}}

{{/*
Return backend imagePullPolicy
*/}}
{{- define "backend.imagePullPolicy" -}}
{{- if .Values.image }}
{{ .Values.image.pullPolicy }}
{{- else -}}
{{ .Values.global.backend.image.pullPolicy }}
{{- end -}}
{{- end -}}

{{/*
Render full env for backend
*/}}
{{- define "backend.renderEnv" -}}
{{ $env := merge .Values.env .Values.global.backend.env }}
{{- if $env }}
env:
{{- range $key, $value := $env }}
  - name: {{ $key }}
    value: {{ $value | quote }}
{{- end }}

{{- $extraEnv := .Values.global.backend.extraEnv -}}

{{- if $extraEnv }}
  {{- toYaml $extraEnv | nindent 2 }}
{{- end }}
{{- end }}
{{- end -}}

{{/*
Get value from env
Usage: `backend.getEnv ( dict "key" CONTAINER_PORT "context" . )`
*/}}
{{- define "backend.getEnv" -}}
{{ $env := merge .context.Values.env .context.Values.global.backend.env }}
{{- index $env .key -}}
{{- end -}}

{{/*
Render init container for migrations waiting
*/}}
{{- define "backend.waitMigrationsInitContainer" -}}
- name: {{ include "common.names.fullname" . }}-wait-migrations
  image: {{ include "backend.image" . }}
  imagePullPolicy: {{ include "backend.imagePullPolicy" . }}
  command:
  - python
  - manage.py
  - migrate
  - --check
  {{- include "backend.renderEnv" . | nindent 2 }}
  {{- if .Values.resources }}
  resources: {{- toYaml .Values.resources | nindent 4 }}
  {{- end }}
{{- end -}}
